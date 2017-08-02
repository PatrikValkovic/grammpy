#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .GrammpyException import GrammpyException


class RuleException(GrammpyException):
    def __init__(self, rule):
        super().__init__()
        self.rule = rule
