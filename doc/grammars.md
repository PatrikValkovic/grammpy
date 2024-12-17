# Grammars handling

All the operation with the grammars are made through the `Grammar` class.

```python
from grammpy import Grammar

g = Grammar()
```

## Terminals

Terminal can be any Python object. For example terminal could be build-in type, class or object.

Terminals are handled using `terminals` property on the grammar.The property inherits from `set` with all its methods available, including set operations. The `add`, `remove` and `discard` methods can accept multiple parameters. Optionally, but more idiomatically, you can pass the terminals to the grammar through the constructor.

```python
from grammpy import Grammar

# 0, 1, and 2 are terminals 
g = Grammar(terminals=[0, 1, 2])

# check if terminal is in the grammar
assert 0 in g.terminals

# remove terminal from the grammar, throws KeyError if terminal is not in the grammar
g.terminals.remove(0)

# removing terminal from the grammar without KeyError
g.terminals.discard(0)

# add multiple terminals
g.terminals.add(0, 4)
```

️⚠️ The library sorts and works with terminals based on their hash code. It, therefore, treats objects with the same hash code as same terminal. If you want to have terminal "instances", e.g. terminal representing number, you need to override the hash method so the parsers know which terminal it is. More information is given in advanced topics in this document.

## Nonterminals

Nonterminals **must** be classes that **must** inherit from `Nonterminal` class. Nonterminals are handled using `nonterminals` property on the Grammar class. The API for the nonterminals is same as for terminals.

```python
from grammpy import Grammar, Nonterminal

class Nonterm1(Nonterminal):
    pass
class Nonterm2(Nonterminal):
    pass
    
# create the grammar
g = Grammar(nonterminals=[Nonterm1, Nonterm2])

# remove both nonterminals from the grammar
g.nonterminals.remove(Nonterm1, Nonterm2)

# return back Nonterm2
g.nonterminals.add(Nonterm2)
```

Unlike terminal property, nonterminal raise `grammpy.exception.NotNonterminalException` exception, if the parameter does not inherit from `Nonterminal` class.


## Rules

As for nonterminals, rules **must** inherit from `grammpy.Rule` class. Rules are handled by the `rules` property of the grammar. Similar to the nonterminals, methods raise `grammpy.exception.NotRuleException` if the parameter doesn't inherit from the `Rule` class.

```python
from grammpy import Rule

class MyRule(Rule):
    pass
```

Each rule class can represent one or more rules in the grammar. Rules are specified by class properties.
The properties are `rules`, `rule`, `left`, `right`, `fromSymbol`, `toSymbol`.
The values are following:
- `fromSymbol` specify symbol on the left side of the rule. Only one value is permitted.
- `toSymbol` specify symbol on the right side of the rule. Only one value is permitted.
- `left` specify the symbols on the left side of the rule. The value needs to be list of individual symbols (terminals or nonterminals).
- `right` specify the symbols on the right side of the rule. The value needs to be list of individual symbols (terminals or nonterminals).
- `rule` specify single rule. The value needs to be tuple containing `left` and `right` symbols (see example).
- `rules` specify multiple rules. The value must be list of `rule` tuples (see example).

```python
from grammpy import Rule

# specify two rules
# MyNonterminal => a MyNonterminal
# AnotherNonterm => MyNonterminal
class FirstRule(Rule):
    rules = [
        ([MyNonterminal], ['a', MyNonterminal]),
        ([AnotherNonterm], [MyNonterminal])
    ]

# specify single rule MyNonterminal => a MyNonterminal
class SecondRule(Rule):
    rule = ([MyNonterminal], ['a',MyNonterminal])
    
# specify single rule MyNonterminal => a MyNonterminal
class ThirdRule(Rule):
    left = [MyNonterminal]
    right = ['a', MyNonterminal]
    
# specify single rule AnotherNonterm => MyNonterminal
class FourthRule(Rule):
    fromSymbol = AnotherNonterm
    toSymbol = MyNonterminal
```

You can choose with approach do you want to use. However, you need to specify the rule using only one of the approaches above. That means, you can't combine `rules` with `rule` or `left`, `rule` with `fromSymbol` etc. You can combine `left` with `toSymbol` and `fromSymbol` with `right`.

```python
# specify single rule MyNonterminal => a MyNonterminal
class FifthRule(Rule):
    fromSymbol = MyNonterminal
    right = ['a', MyNonterminal]
```

The rest of the attributes are dynamically evaluated when possible. For example, you can't get `rule` from `rules` when you defined multiple rules, but you can get `rules` from `rule` definition. In case you try to get value for attribute that is not possible to dynamically evaluate, exception is raised.

> ⚠️ When the class defines multiple rules, it is automatically split by the `Grammar` class. See bellow for more info.

This is useful when you write your own algorithm and want to use uniform approach. 


```python
class FourthRule(Rule):
    fromSymbol = MyNonterminal
    right = ['a', MyNonterminal]

assert FourthRule.left == [MyNonterminal]
assert FourthRule.rule == ([MyNonterminal], ['a', MyNonterminal])
assert FourthRule.rules == [([MyNonterminal], ['a', MyNonterminal])]

FourthRule.toSymbol  # raise NotASingleSymbolException
```

When the grammar handling rules, multiple exceptions can occur.
- `RuleNotDefinedException` - rule is not defined.
- `RuleSyntaxException` - rule syntax is invalid. This exception is base class for all the following exceptions.
- `MultipleDefinitionException` - the rules is defined multiple time (for example using `rule` and `rules` property at the same time).
- `UselessEpsilonException` - epsilon is used wrong way.
- `TerminalDoesNotExistsException` - terminal doesn't exist in the grammar. This can occur only when you add the rule into the grammar.
- `NonterminalDoesNotExistsException` - nonterminal doesn't exist in the grammar. This can occur only when you add the rule into the grammar.

The grammar automatically handles rules with their symbols. That means when the symbol (terminal or nonterminal) is removed, all rules with that symbol are removed as well.

```python
from grammpy import Nonterminal, Rule, Grammar

class MyNonterminal(Nonterminal):
    pass

class MyRule(Rule):
    rule = ([MyNonterminal],['a',MyNonterminal])
    
g = Grammar(terminals=['a'],
            nonterminals=[MyNonterminal],
            rules=[MyRule])
assert g.rules.size() == 1
g.nonterminals.remove(MyNonterminal)
assert g.rules.size() == 0
assert MyRule not in g.rules
``` 

## Epsilon

The library has special symbol for epsilon, allowing you to use None as a terminal. It uses two forms (short and long), that are equal to each other.

```python
from grammpy import Rule, EPS, EPSILON

class MyRule1(Rule):
    rule = ([MyNonterminal],[EPS])
    
class MyRule2(Rule):
    rule = ([MyNonterminal],[EPSILON])
```


## Start symbol

For the start (or beginning) symbol, grammar defines the `start` property. Start symbol needs to be nonterminal present in the grammar.

```python
from grammpy import Grammar, Nonterminal

class MyNonterminal(Nonterminal): pass

g = Grammar(nonterminals=[MyNonterminal],
            start_symbol=MyNonterminal)
            
assert MyNonterminal is g.start
del g.start
assert g.start is None
g.start = MyNonterminal
```

When nonterminal used as start symbol is removed, start symbol will be set to None.

## Grammar creation

It is possible to fill grammar using constructor, which accepts list of terminals, nonterminals, rules and start symbol. This is the preferred and idiomatic way to do so.

```python
g = Grammar(terminals = [0, 1, 'a', 'b'],
            nonterminals=[A, B],
            rules=[RuleATo0B, RuleBtoab],
            start_symbol=A)
```

## Backward compatibility

The library interface changed between version 1 and 2. The decision was make to make the interface more python-like. If you have already written the application using the old interface, you can still use it with a bit of changes.

> ⚠️ The old interface is deprecated and will be removed in the future.

The only change is to switch the `grammpy.Grammar` class implementation with the `grammpy.old_api.Grammar` one. There are no more changes needed. The library then works the same as in the version 1.

To make the transition easier, the `grammpy.old_api.Grammar` implements both interfaces from version 1 as well from version 2. So you can start rewriting your applications gradually and then switch the Grammar classes when you need.

The drawback of using the old interface is it's performance. The backward-compatible facade calls the new interface under the hood, and as so the performance is a bit worse. It's so highly recommended to switch to the new interface as soon as possible.

## Advanced topics

Follows advanced topics how the library handles the grammars. You may first explore other library use cases and topics before you dive deeper here. The following topics assume knowledge on how the rest of the library works.

### Rules splitting

To work with the rules a bit easier the `Grammar` class split class with multiple rules (defined by `rules` property) to multiple rule class, that inherits from the `grammpy.representation.support.SplitRule`. You don't need to care about it as long as you work with the grammar. However, when you parse the input, the `SplitRule` classes will be instantiated instead. You may use static method `splitted_rules` on the class `grammpy.transforms.InverseCommon`, to replace `SplitRule` classes with the original rule. For more see [transformation documentation](transforms.md).

```python
from grammpy import *
from grammpy.representation.support import SplitRule
from grammpy.transforms import InverseCommon
from grammpy.parsers import cyk

class A(Nonterminal): pass
class MyRule(Rule):
    rules = [
        ([A], [0]),
        ([A], [1])
    ]
    
g = Grammar(terminals=[0, 1],
            nonterminals=[A],
            rules=[MyRule],
            start_symbol=A)

# all operations works on splitted rule
assert MyRule in g.rules

# will instantiate SplitRule
root = cyk(g, [0])
assert isinstance(root.to_rule, SplitRule)

# use MyRule instead
root = InverseCommon.splitted_rules(root)
assert isinstance(root.to_rule, MyRule)
```

### Input data for terminals

As stated at the beginning, terminals are handled by their hash. Two objects with the same hash are considered to be same. This way, you can define own class with properties as you need and use class hash value for the instances. In the parsing stage, you can then pass instances instead of class itself.

```python
from grammpy import *
from grammpy.parsers import cyk

# define custom terminal
class CustomTerminal:
    def __init__(self, values):
        self.values = values
    # hashes if the instances will be same
    def __hash__(self):
        return hash(CustomTerminal)

# define nonterminal
class A(Nonterminal):
    pass
    
# define rule A => CustomTerminal
class MyRule(Rule):
    rule = ([A], CustomTerminal)  # Treated as type


g = Grammar(terminals=[CustomTerminal],
            nonterminals=[A],
            rules=[MyRule],
            start_symbol=A)
       
# parse input     
root = cyk(g, [CustomTerminal(5)])  # Treated as instance
# leaf will contain the instance with value 5
```