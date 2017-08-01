#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .Rule import Rule

class IsMethodsRuleExtension(Rule):

    @classmethod
    def is_regular(cls):
        return False

    @classmethod
    def is_contextfree(cls):
        return False

    @classmethod
    def is_context(cls):
        return False

    @classmethod
    def is_unrestricted(cls):
        return False