#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .Rule import Rule
from .exceptions.RuleException import RuleException


class IsMethodsRuleExtension(Rule):
    @classmethod
    def is_regular(cls):
        raise NotImplementedError()

    @classmethod
    def is_contextfree(cls):
        raise NotImplementedError()

    @classmethod
    def is_context(cls):
        raise NotImplementedError()

    @classmethod
    def is_unrestricted(cls):
        raise NotImplementedError()

    @classmethod
    def validate(cls, grammar):
        raise NotImplementedError()

    @classmethod
    def is_valid(cls, grammar):
        try:
            cls.validate(grammar)
            return True
        except RuleException:
            return False
