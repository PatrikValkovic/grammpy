#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .RuleException import RuleException

class RuleSyntaxException(RuleException):
    def __init__(self, rule, message):
        super().__init__(rule)
        self.message = message

