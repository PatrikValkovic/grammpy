# pyparsers [![Build Status](https://travis-ci.org/PatrikValkovic/pyparsers.svg?branch=dev)](https://travis-ci.org/PatrikValkovic/pyparsers) [![Coverage Status](https://coveralls.io/repos/github/PatrikValkovic/pyparsers/badge.svg?branch=dev)](https://coveralls.io/github/PatrikValkovic/pyparsers?branch=dev)

Library implements CYK algorithm.
It uses grammpy library for grammar specification.

Only exposed method is `cyk`.

```python
from pyparsers import cyk

g = Grammar()
# ...

parsed = cyk(g, [*input])
```

-----

Version: dev

Author: Patrik Valkovič

Licence: GNU General Public License v3.0
