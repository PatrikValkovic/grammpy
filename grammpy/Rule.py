#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .Constants import EPSILON


class Rule:
    # TODO rules -> rule -> left/right -> fromSymbol/toSymbol -> rules
    """
    fromSymbol = EPSILON
    toSymbol = EPSILON
    right = [EPSILON]
    left = [EPSILON]
    rule = ([EPSILON], [EPSILON])
    rules = [([EPSILON], [EPSILON])]
    """

    fromSymbol = None
    toSymbol = None
    right = None
    left = None
    rule = None
    rules = None

    __active = True

    @staticmethod
    def is_regular():
        return False

    @staticmethod
    def is_contextfree():
        return False

    @staticmethod
    def is_context():
        return False

    @staticmethod
    def is_unrestricted():
        return False

    @classmethod
    def rules_count(cls):
        return len(cls.rules)
