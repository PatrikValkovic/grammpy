#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 14:47
:Licence GNUv3
Part of pyparsers

"""

from typing import Iterable
from grammpy import *
from .Field import Field

def cyk(grammar: Grammar, input: Iterable) -> Nonterminal:
    i = list(input)
    f = Field(grammar, len(i))
    raise NotImplementedError()