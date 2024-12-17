#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:52
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:  # pragma no cover
    from typing import TypeAlias

class _Epsilon:
    def __repr__(self):
        return 'EPSILON'  # pragma no cover
    def __str__(self):
        return 'EPSILON'  # pragma no cover

EPSILON = _Epsilon()
EPS = EPSILON

EPSILON_TYPE = type(EPSILON)  # type: TypeAlias

class _EndOfInput:
    def __repr__(self):
        return 'END_OF_INPUT'  # pragma no cover
    def __str__(self):
        return 'END_OF_INPUT'  # pragma no cover

END_OF_INPUT = _EndOfInput()
EOI = END_OF_INPUT

END_OF_INPUT_TYPE = type(END_OF_INPUT)  # type: TypeAlias
