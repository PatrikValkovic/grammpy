# grammpy

Current version: 1.1.6

[![Build Status](https://travis-ci.org/PatrikValkovic/grammpy.svg?branch=master)](https://travis-ci.org/PatrikValkovic/grammpy)
[![Coverage Status](https://coveralls.io/repos/github/PatrikValkovic/grammpy/badge.svg?branch=master)](https://coveralls.io/github/PatrikValkovic/grammpy?branch=master)

Package for representing formal grammars.

## Usage

First of all, you need to create grammar

```python
from grammpy import Grammar

g = Grammar()
```

### Terminals and nonterminals

Then you need to add terminals and nonterminals into Grammar. 
Terminals could be arbitrary entity, but nonterminal must inherit from Nonterminal class.

```python
from grammpy import Grammar, Nonterminal

g = Grammar()
g.add_term(0)       # separate
g.add_term([1, 2])  # or even in array
g.add_term(['asdf', MyClass])

class MyNonterminal(Nonterminal):
    pass
    
g.add_nonterm(MyNonterminal)
```

Terminal could be build-in type, class or object. Objects with same hash code are considered as same.

Nonterminals **must** be classes and **must** inherit from Nonterminal class. 
API for nonterminals is the same as for terminals.

#### Additional methods

Of course you can check, if the terminal is already in grammar or you can remove terminals.
(the same for nonterminals).

```python
g.have_term(0) # check if the terminal is in the grammar
g.have_term([0, 'a', 'asdf']) # check if all terminals in array are in grammar
g.remove_term(['a',0]) # remove terminals from grammar
g.remove_term() # remove all terminals without parameter
```

The `get_term` method returns Terminal object, that has actual terminal under Symbol property.

```python
a = g.get_term('a') # returns terminal object
a.symbol() == a.s == 'a'
a = g.term('a') # equal

all = g.get_term() # returns array with all terminals
some = g.term(['a', 0, 'b']) # when array is passed, returns array
some[0].s == 'a'
some[1].s == 0
some[2] == None # when terminal is not found, returns None
```

Methods for adding (`add_term`) and removing (`remove_term`) returns list of added/deleted entities.
Only entities that are really add/remove are return (duplicate entities are ignored).

```python
g = Grammar()
add = g.add_term([1, 2])
add[0].s == 1 and add[1].s == 2
rem = g.remove_term(['a',1]) # 'a' is not in grammar
rem[0].s == 1
```

The same API is for nonterminals and also for rules.

### Rules

As for nonterminals, rules must inherit from Rule class

```python
from grammpy import Rule

class MyRule(Rule):
    pass
```

Each rule class could represent one or more rules. 
Rules are specified by properties of class.



```python
from grammpy import Rule

class FirstRule(Rule):
    rules = [([MyNonterminal],['a',MyNonterminal]),
             ([AnotherNonterm],[MyNonterminal])]
    
class SecondRule(Rule):
    rule = ([MyNonterminal],['a',MyNonterminal])
    
class ThirdRule(Rule):
    left = [MyNonterminal]
    right = ['a',MyNonterminal]
    
class FourthRule(Rule):
    fromSymbol = AnotherNonterm
    toSymbol = MyNonterminal
```

Its enough to use only situation, rest is automatically computed.
You can also combine approaches (side and symbol approach).

```python
class FourthRule(Rule):
    fromSymbol = MyNonterminal
    right = ['a',MyNonterminal]

FourthRule.rules == [([MyNonterminal],['a',MyNonterminal])]
``` 

### Epsilon

Grammpy has special symbol for epsilon, because None could be also used as terminal.
You can use shorter or longer forms, they are equal.

```python
from grammpy import Rule, EPS, EPSILON

class MyRule(Rule):
    rule = ([MyNonterminal],[EPS])
```

### Start symbol

You can manipulate with start symbol with following API:

```python
g.start_set(NONTERM)
g.start_isSet() == true
g.start_is(NONTERM) == true
g.start_get == NONTERM
```

Symbol for start symbol must be in grammar's nonterminals first.

### Grammar creation

It is possible to fill grammar with constructor, which accepts list of terminals, nonterminals, rules and start symbol.

```python
g = Grammar(terminals = [0, 1, 'a', 'b'],
            nonterminals=[A, B],
            rules=[RuleATo0B, RuleBtoab],
            start_symbol=A)
```

## Correctness

This library handles invalid rules
(in situations when terminal/nonterminal is not defined in grammar or rule is syntactically invalid),
but does not handle division to grammar sets (like contextfree or regular grammar).

Library that will deal with obedience or transformations into another type of grammar is in development.

## Roadmap

- Improve API, so library will be more usable and also more understandable.
- Add layer so terminals, nonterminals and rules could be add in simple string.
- Add additional API into Rule class, so you can simply check type of rule.

There are also additional libraries in development, that will integrate with this library.

-----

Author: Patrik Valkovič

Licence: GNU General Public License v3.0