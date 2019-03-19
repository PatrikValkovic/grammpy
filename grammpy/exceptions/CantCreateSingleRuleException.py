#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 08:54
:Licence MIT
Part of grammpy

"""

from .RuleException import RuleException


class CantCreateSingleRuleException(RuleException):
    """
    From Rule class with multiple rules defined library was unable to split separate rules
    """
    def __init__(self, rules):
        self.rules = rules
