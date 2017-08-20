#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 20:29
:Licence GNUv3
Part of grammpy

"""

from copy import deepcopy
from inspect import isclass
from .RulesRemovingGrammar import RulesRemovingGrammar as Grammar
from ..Nonterminal import Nonterminal
from ..Rules import Rule
from ..Constants import EPSILON

class CopyableGrammar(Grammar):
    pass
