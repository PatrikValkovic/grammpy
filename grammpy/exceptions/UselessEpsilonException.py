#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class UselessEpsilonException(RuleSyntaxException):
    def __init__(self, rule):
        super().__init__(rule)
