#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:25
:Licence GNUv3
Part of grammpy

"""

from .RuleException import RuleException

class RuleSyntaxException(RuleException):
    """
    Syntax of the rule or rules is invalid
    """
    def __init__(self, rule, message, additional = None):
        super().__init__(rule)
        self.message = message
        self.additional = additional

