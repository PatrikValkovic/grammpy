#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:51
:Licence GNUv3
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class UselessEpsilonException(RuleSyntaxException):
    """
    Exception that exception used in grammar is useless
    """
    def __init__(self, rule):
        super().__init__(rule, 'Usage of epsilon in this context if useless')
