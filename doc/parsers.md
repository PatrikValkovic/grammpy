# Parsers

So far, library only implements CYK algorithm.
More algorithms like LL, LR and GLR are in the roadmap.

The parsing algorithms are in the `grammpy.parsers` package.


## General approach

All the parsing algorithms construct tree structure.
The tree structure reflects the grammar provided.

In the tree, the parser **instantiates** nonterminals and rules to construct the tree.
The parsers don't instantiate the terminals, because they use the input sequence.
However, to be able to connect them to the tree, the parsers create `grammpy.Terminal` class.
This class have `symbol` method (respectively `s` property`) that returns the symbol from the input.

The parsers always returns root node of the tree.
You can traverse the tree using following properties.
- `to_rule` on Nonterminal and Terminal class to get rule that they rewrite to.
- `from_rule` on Nonterminal or Terminal class to get rule that they rewrite from.
- `to_symbols` on Rule to get list of symbols that the rule rewrite to.
- `from_symbols` on Rule to get list of symbols that the rule rewrite from.

For more advanced traversing, see [traversing documentation](helpers.md).

### Working with the tree

As noted, the parsers instantiate the Nonterminal and Rule classes.
They then returns root of the parsed tree to the user.

This approach have huge flexibility, as the semantic part of the parsing is fully in your hands.
You are free to define methods and properties on the objects and then use them. 
Take for example grammar, where you should handle plus operation. 
You can define nonterminal like this.

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

Then, you can use one of the traversing methods (see [traversing](helpers.md)) or run the algorithm on your own to compute values of all the nodes.
You can as well redefine the ValueNonterminal as follow and call recursion.

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

The library helps you with the syntax check and parsing, but the whole semantic part is fully in your hands.

## Cyk

Only exposed method is `cyk`.
The method accepts grammar and input sequence as an input.

It raise `NotParsedException` if input sequence was syntactically invalid and CYK was unable to parse it.
It raise `StartSymbolNotSetException` if the grammar doesn't have start symbol set up.

```python
from pyparsers import cyk

g = Grammar()
# ... fill out the grammar

root = cyk(g, [0, 1, 2])
```
