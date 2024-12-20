# Parsers

So far, library implements CYK and LL(k) algorithms. More algorithms like LR and GLR are in the roadmap.

The parsing algorithms are in the `grammpy.parsers` package.


## General approach

All the parsing algorithms construct tree structure that I will call abstract syntax tree (AST) through the rest of the text. The tree structure reflects the provided grammar.

In the tree, the parser **instantiates** nonterminals and rules to construct the tree. The parsers don't instantiate the terminals, because they should be already in the input sequence. 
However, to be able to connect them to the tree, the parsers create `Terminal` class if the element in input sequence is not already its instance (or instance of subclass).
This class have `symbol` method (respectively `s` property`) that returns the symbol from the input.

Epsilon symbol is treated similarly to terminals. It is connected to the AST as instance of `Terminal` class but the symbol is `grammpy.EPSILON` symbol.

The parsers always returns root node of the tree.
You can traverse the tree using following properties.
- `to_rule` on instances of Nonterminal and Terminal classes to get rule that they were rewritten to.
- `from_rule` on instances of Nonterminal or Terminal classes to get rule that they rewrite from.
- `to_symbols` on instance of Rule class to get list of symbols that the rule rewrites to.
- `from_symbols` on instance of Rule class to get list of symbols that the rule is rewritten from.

For more advanced traversing, see [traversing documentation](helpers.md).

### Working with the tree

As noted, the parsers instantiate the Nonterminal and Rule classes provided to the grammar. They then returns root of the parsed tree to the user.

This approach have huge flexibility, as the semantic part of the parsing is fully in your hands. You are free to define methods and properties on the objects and then use them. Take for example grammar, where you should handle plus operation. You can define nonterminal like this.

```python
class ValueNonterminal(Nonterminal):
    def __init__(self):
        self.value = None
```

Then you can define following rule, that will compute the value of the parent node.

```python
class PlusRule(Rule):
    rule = ([ValueNonterminal], [ValueNonterminal, '+', ValueNonterminal])
    def compute_value(self):
        parent = self.from_symbols[0]
        child1 = self.to_symbols[0]
        child2 = self.to_symbol[1]
        parent.value = child1.value + child2.value
```

Then, you can use one of the traversing methods (see [traversing](helpers.md)) or run the algorithm on your own to compute values for all the nodes.

> ⚠️ It is recommended to use the traversing code provided instead of using recursion. The traversing implementation has special recursion syntactically similar to recursion while avoiding it directly, allowing you to traverse even very deep trees without causing the stack overflow error.

You can as well redefine the ValueNonterminal as follows and call recursion.

```python
class ValueNonterminal(Nonterminal):
    def __init__(self):
        self._value = None
        
    @property
    def value(self):
        if self._value is None:
            self.to_rule.compute_value()
        return self._value
        
    @value.setter
    def value(self, value):
        self._value = value
```

The library helps you with the syntax check and parsing, but the whole semantic part is fully in your hands using a familiar Python code.

## CYK

Implementation of Cocke–Younger–Kasami parsing algorithm.

The advantage of CYK parser is that it can parse any context-free grammar (after transforming it into Chomsky Normal Form), including ambiguous grammars.

> ⚠️ Although CYK can handle ambiguous grammars, the returned AST is nondeterministic. Although the algorithm can theoretically return all possible ASTs, this is not yet implemented. The returned AST is not guaranteed to be the same for the same input sequence and grammar across multiple runs.

The disadvantage is that it is the slowest algorithm with worse case running time of *Ⲟ(n³·|G|)* time and *Ⲟ(n²·/ 2)* space, where *n* is the length of the input sequence and *|G|* is the size of the grammar. The whole input sequence must fit into memory.

The only exposed method is `cyk`. It accepts grammar in Chomsky Normal Form (see [transformation](transforms.md) for manipulation) and input sequence. Returning single valid AST if the sequence was parsed successfully.

It raises `NotParsedException` if input sequence was syntactically invalid and CYK was unable to parse it.\
It raises `StartSymbolNotSetException` if the grammar doesn't have start symbol set up.

```python
from pyparsers import cyk

g = Grammar()
# ... fill out the grammar

root = cyk(g, [0, 1, 2])
```


## LL(k)

Arbitrary look-ahead or LL(k) grammars is top-down approach to parsing input sequence. Based on the nonterminal on top of the stack and the input sequence of length *k*, the parser decides which rule to apply. The most common implementation is look ahead of 1 or LL(1) parsers.

The advantage of LL(k) parser is that it is faster than CYK parser with *Ⲟ(n)* time and *Ⲟ(|G|)* space, where *n* is the length of the input sequence and *|G|* is the size of the grammar. Only the look ahead sequence (*k* terminals) from the input sequence must fit into the memory allowing you to use generators for parsing.

The disadvantage is that it is weaker and can parse only LL(k) grammars. The grammar must be left-factored and left-recursive rules must be eliminated. The provided rules must already satisfy these requirements and there are no grammar transformations operations for these implemented yet.

LL(k) grammars parse input based on the parsing table specifying the rule to apply based on the nonterminal on top of stack and the *k* terminals in the look ahead. The library can construct the table for you.

### First table

First, you need to create FIRST table specifying what terminals can each nonterminal generate. The first table can be generated using `ContextFree.create_first_table` method.

```python
from grammpy import Grammar
from grammpy.transforms import ContextFree

g = Grammar()
first_table = ContextFree.create_first_table(g, look_ahead=1)
```

The table is dictionary with Nonterminals as keys and set of sequences of length max *k* that the nonterminals generates. The sequences are stored as tuples with exception if `EPSILON` symbol, that is in the set inserted directly.

Note that the FIRST table may contain sequences shorter than *k*.

### Follow table

The second table you need to create is FOLLOW table. The table specifies what terminals can follow the nonterminal in the sequence. The follow table can be generated using `ContextFree.create_follow_table` method.

```python
from grammpy import Grammar
from grammpy.transforms import ContextFree

g = Grammar()
first_table = ContextFree.create_first_table(g, look_ahead=1)
follow_table = ContextFree.create_follow_table(g, first_table, look_ahead=1)
```

The look ahead must be same or shorter than for first tale. The returned value is dictionary with Nonterminals as keys and set of terminals that can follow the nonterminal. All sequences in set has length exactly *k* and are padded with special symbol `grammpy.END_OF_INPUT` (or its shorter alias `grammpy.EOI`) if shorter.

### Parsing table

From FIRST and FOLLOW tables the library can generate parsing table for you using `grammpy.parsers.create_ll_parsing_table` function.

```python
from grammpy import Grammar
from grammpy.transforms import ContextFree
from grammpy.parsers import create_ll_parsing_table

g = Grammar()
first_table = ContextFree.create_first_table(g, look_ahead=1)
follow_table = ContextFree.create_follow_table(g, first_table, look_ahead=1)
parsing_table = create_ll_parsing_table(g, first_table, follow_table, look_ahead=1)
```

The parsing table is multilayer dictionary with keys `parsing_table[top_of_stack_nonterminal][look_ahead_tuple]` returning rule (or set of rules, more on this later) to apply in such situation.

You can store this table (e.g. using *pickle* package) and reuse it across runs if the grammar doesn't change, allowing you to skip all the operations above.

### Parsing

Finally, all you need to call `grampy.parsers.ll` function passing it the starting symbol, input sequence, and the parsing table.

```python
from grammpy import Grammar
from grammpy.transforms import ContextFree
from grammpy.parsers import create_ll_parsing_table, ll

g = Grammar()
first_table = ContextFree.create_first_table(g, look_ahead=1)
follow_table = ContextFree.create_follow_table(g, first_table, look_ahead=1)
parsing_table = create_ll_parsing_table(g, first_table, follow_table, look_ahead=1)
root =  ll(g.start, [1, '+', 3], parsing_table, look_ahead=1),
```

The function returns the root of the AST, or raise exception if error occurred.

### Ambiguity

The provided grammar may be ambiguous. E.g. think about this typical C-like condition syntax.

```cpp
if(x > 0)
if(x < 10)
else
```

Does the `else` branch bellow to the first or second conditions? That is usually not apparent from the syntax.

Sometimes, the ambiguity may be caused just by too short look ahead.

Because of this, the `create_ll_parsing_table` methods has set of rules as value in the parsing table, allowing you to do some post-process and remove the ambiguity as you see fit.

The `ll` function will by default raise exception when the ambiguity is detected (it receives set with multiple possible rules). You can disable this behavior by setting `raise_on_ambiguity=False` parameter. 

```python
from grammpy.parsers import ll

root =  ll(g.start, [1, '+', 3], parsing_table, look_ahead=1, raise_on_ambiguity=False),
```

### Errors

All the error for look-ahead parser inherit from `grammpy.exceptions.LLParsingException`. This class has additional attribute `position` specifying at which index of the input sequence the error occurred.

The parsing can also raise following exceptions:
- `grammpy.exceptions.NonterminalIsMissingException`: Exception that occurs when there is nonterminal on top of the stack that has no entry in the parsing table.
- `grammpy.exceptions.NoRuleForLookAhheadException`: There is no rule to apply for the nonterminal and look ahead.
- `grammpy.exceptions.ParsingAmbiguityException`: There are multiple rules to apply for the nonterminal and look ahead.
- `grammpy.TableDisrepancyException`: Exception raised when the nonterminal on the stack doesn't match the nonterminal in the input sequence. In general points to discrepancy between the parsing table and the rule within it.
- `grammpy.exception.NotRuleException`: Exception raised when the rule in the parsing table is not instance of Rule class. Doesn't inherit from the `LLParsingException` class but directly from `GrammpyException`.

### Custom parsing table

You don't necessary need to use parsing table generated by `create_ll_parsing_table` function, but you can create your. The parsing table is just two dictionaries within each other. The library calls it the following way:

```python
parsing_table[nonterminal_type_on_top_of_stack][tuplf_of_size_k_as_lookahead]
```

The return value must be Rule to apply (or set of multiple rules if you know what you are doing).

This allows you to provide your own implementation as long as you keep the interface intact (e.g. using `__getitem__` magic method to let instance behave like a dictionary). E.g. you may want to "compact" the parsing table such that the full lookahead *k* is necessary only in specific cases, but in the majority of time only single symbol in look ahead is enough. The implementation can then look only at the first symbol in look ahead and decide to expand the search further only if ambiguity is detected. This allows you to reduce the size of the parsing table and have it expanded only in the necessary cases.

The compaction algorithm is not yet implemented in the library.
