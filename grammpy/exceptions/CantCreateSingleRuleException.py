#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 08:54
:Licence GNUv3
Part of grammpy

"""

from .RuleException import RuleException


class CantCreateSingleRuleException(RuleException):
    def __init__(self, rules):
        self.rules = rules
