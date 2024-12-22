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
        return 'EPSILON'
    def __str__(self):
        return 'EPSILON'
    def __reduce__(self):
        return _get_epsilon_instance, ()

EPSILON = _Epsilon()
EPS = EPSILON

EPSILON_TYPE = type(EPSILON)  # type: TypeAlias

def _get_epsilon_instance():
    return EPSILON


class _EndOfInput:
    def __repr__(self):
        return 'END_OF_INPUT'
    def __str__(self):
        return 'END_OF_INPUT'
    def __reduce__(self):
        return _get_end_of_input_instance, ()

END_OF_INPUT = _EndOfInput()
EOI = END_OF_INPUT

END_OF_INPUT_TYPE = type(END_OF_INPUT)  # type: TypeAlias

def _get_end_of_input_instance():
    return END_OF_INPUT
