#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:24
:Licence MIT
Part of grammpy

"""

from .GrammpyException import GrammpyException


class RuleException(GrammpyException, ValueError):
    """
    Error with the rule or rules
    """
    def __init__(self, rule):
        super().__init__()
        self.rule = rule
