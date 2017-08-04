# grammpy

Current version: 0.1.0

[![Build Status](https://travis-ci.org/PatrikValkovic/grammpy.svg?branch=dev)](https://travis-ci.org/PatrikValkovic/grammpy)
[![Coverage Status](https://coveralls.io/repos/github/PatrikValkovic/grammpy/badge.svg?branch=dev)](https://coveralls.io/github/PatrikValkovic/grammpy?branch=dev)

Package for representing formal grammars.

## Usage

First at all, you need to create grammar

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

Terminal could be build-in type, class or object. Objects with same hash code are consider as same.

Nonterminals **must** be classes and **must** inherit from Nonterminal class. 
API for nonterminals is the same as for terminals.

#### Additional methods

Of course you can check, if is terminal already in grammar or remove terminals
(the same for nonterminals).

```python
g.have_term(0) # check if is terminal in grammar
g.have_term([0, 'a', 'asdf']) # check is all terminals in array are in grammar
g.remove_term(['a',0]) # remove terminals from grammar
g.remove_term() # withour parameter remove all terminals
```

The `get_term` method return Terminal object, that have actual terminal under Symbol property.

```python
a = g.get_term('a') # return terminal object
a.symbol() == a.s == 'a'
a = g.term('a') # equal

all = g.get_term() # return array with all terminals
some = g.term(['a', 0, 'b']) # when is array passed, returns array
some[0].s == 'a'
some[1].s == 0
some[2] == None # when terminal is not find, returns None
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
Rules are specified by properties on class.



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

Its enough to use only situation, rest are automatically computed.
You can also combine approaches (side and symbol approach).

```python
class FourthRule(Rule):
    fromSymbol = MyNonterminal
    right = ['a',MyNonterminal]

FourthRule.rules == [([MyNonterminal],['a',MyNonterminal])]
``` 

### Epsilon

Grammar have special symbol for epsilon, because also None could be use as terminal.
You can use shorter or longer forms, they are equal.

```python
from grammpy import Rule, EPS, EPSILON

class MyRule(Rule):
    rule = ([MyNonterminal],[EPS])
```

## Correctness

This library handle invalid rules 
(in situations when terminal/nonterminal is not defined in grammar or rule is syntactically invalid),
but not handle obedience into grammar's sets (like contextfree or regular grammar).

Library that will deal with obedience or transformations into another type of grammar is in development.

## Roadmap

- Improve API, so library will be more usable and also more understandable.
- Add layer so terminals, nonterminals and rules could be add in simple string.
- Add additional API into Rule class, so you simply check type of rule.

There are also additional libraries in development, that will integrate with this library.

-----

Author: Patrik Valkovič

Licence: GNU General Public License v3.0