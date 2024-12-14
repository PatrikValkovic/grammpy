# grammpy

Current version: 2.0.0

[![Build Status](https://www.travis-ci.com/PatrikValkovic/grammpy.svg?branch=master)](https://www.travis-ci.com/PatrikValkovic/grammpy)
[![Coverage Status](https://coveralls.io/repos/github/PatrikValkovic/grammpy/badge.svg?branch=master)](https://coveralls.io/github/PatrikValkovic/grammpy?branch=master)

Package for representing formal grammars.
Contains algorithms to work with a grammars and parse them.

## Installation

If you are using `pip`, simple run following command.
```
pip install grammpy
```

You can install the package from the repository as well.
```
git clone https://github.com/PatrikValkovic/grammpy.git
cd grammpy
python setup.py install
```

## Usage

Defining a grammar doesn't require special tools anymore.
All what you need is just an IDE and you have the full support.

Let's define grammar using standard Python objects instead.

```python
from grammpy import *
from grammpy.transforms import ContextFree, InverseContextFree
from grammpy.parsers import cyk


class Number:
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return hash(Number)


class PlusNonterminal(Nonterminal):
    @property
    def value(self):
        return self.to_rule.get_value()


class PlusRule(Rule):
    rule = ([PlusNonterminal], [PlusNonterminal, '+', PlusNonterminal])
    def get_value(self):
        child1 = self.to_symbols[0]
        child2 = self.to_symbols[2]
        return child1.value + child2.value


class RewriteRule(Rule):
    fromSymbol = PlusNonterminal
    toSymbol = Number
    def get_value(self):
        return self.to_symbols[0].s.value


g = Grammar(terminals=[Number, '+'],
            nonterminals=[PlusNonterminal],
            rules=[PlusRule, RewriteRule],
            start_symbol=PlusNonterminal)
ContextFree.prepare_for_cyk(g, inplace=True)
root = cyk(g, [Number(5), '+', Number(3), '+' , Number(8)])
root = InverseContextFree.reverse_cyk_transforms(root)
assert root.value == 16
```

## Documentation

You can read more about the library in the [doc](doc) directory.

## Examples

You can view some examples in the [examples](examples) directory.

-----

Version: 2.0.0

Author: Patrik Valkovič

Licence: MIT
