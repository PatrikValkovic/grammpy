#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .exceptions import CantCreateSingleRuleException, RuleNotDefinedException, NotASingleSymbolException


class CP(object):
    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls=None):
        return self._getter(cls)  # for static remove cls from the call


class Rule:
    """
    fromSymbol = EPSILON
    toSymbol = EPSILON
    right = [EPSILON]
    left = [EPSILON]
    rule = ([EPSILON], [EPSILON])
    rules = [([EPSILON], [EPSILON])]
    """

    @CP
    def toSymbol(cls):
        if cls.__traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        right = cls.rules[0][1]
        if len(right) > 1:
            raise NotASingleSymbolException(right)
        return right[0]

    @CP
    def fromSymbol(cls):
        if cls.__traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        left = cls.rules[0][0]
        if len(left) > 1:
            raise NotASingleSymbolException(left)
        return left[0]

    @CP
    def right(cls):
        if cls.__traverse:
            return [cls.toSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][1]

    @CP
    def left(cls):
        if cls.__traverse:
            return [cls.fromSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][0]

    @CP
    def rule(cls):
        if cls.__traverse:
            return (cls.left, cls.right)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0]

    @CP
    def rules(cls):
        cls.__traverse = True
        r = cls.rule
        cls.__traverse = False
        return [r]

    __traverse = False

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

    @classmethod
    def count(cls):
        return cls.rules_count()
