# pyparsers [![Build Status](https://travis-ci.org/PatrikValkovic/pyparsers.svg?branch=master)](https://travis-ci.org/PatrikValkovic/pyparsers) [![Coverage Status](https://coveralls.io/repos/github/PatrikValkovic/pyparsers/badge.svg?branch=master)](https://coveralls.io/github/PatrikValkovic/pyparsers?branch=master)

Library implements CYK algorithm.
It uses grammpy library for grammar specification.

Only exposed method is `cyk`.
It raise `NotParsedException` if input sequence was syntactically invalid and CYK was unable to parse it.

```python
from pyparsers import cyk

g = Grammar()
# ...

parsed = cyk(g, [*input])
```

-----

Version: 0.0.1

Author: Patrik Valkovič

Licence: GNU General Public License v3.0
