#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:38
:Licence GNUv3
Part of grammpy

"""

from .Grammars.PrettyApiGrammar import PrettyApiGrammar as Grammar
from .Nonterminal import Nonterminal
from .Rule import Rule

EPSILON = object()
EPS = EPSILON
