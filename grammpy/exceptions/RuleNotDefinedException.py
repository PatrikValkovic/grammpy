#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 08:46
:Licence GNUv3
Part of grammpy

"""

from .RuleException import RuleException


class RuleNotDefinedException(RuleException):
    """
    For Rule class the rule is not defined
    """
    def __init__(self, rule):
        self.rule = rule
