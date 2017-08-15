#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:45
:Licence GNUv3
Part of grammpy

"""

from .exceptions import CantCreateSingleRuleException, RuleNotDefinedException, NotASingleSymbolException


class CP(object):
    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls=None):
        return self._getter(cls)  # for static remove cls from the call


class MetaWithHash(type):
    @staticmethod
    def _lists_to_tuples(lst):
        if not isinstance(lst, list) and not isinstance(lst, tuple):
            return lst
        return tuple(MetaWithHash._lists_to_tuples(item) for item in tuple(lst))

    def __hash__(cls):
        transformed = MetaWithHash._lists_to_tuples(cls.rules)
        return hash(transformed)


class Rule(metaclass=MetaWithHash):
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
        if cls._traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        right = cls.rules[0][1]
        if len(right) > 1:
            raise NotASingleSymbolException(right)
        return right[0]

    @CP
    def fromSymbol(cls):
        if cls._traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        left = cls.rules[0][0]
        if len(left) > 1:
            raise NotASingleSymbolException(left)
        return left[0]

    @CP
    def right(cls):
        if cls._traverse:
            return [cls.toSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][1]

    @CP
    def left(cls):
        if cls._traverse:
            return [cls.fromSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][0]

    @CP
    def rule(cls):
        if cls._traverse:
            return (cls.left, cls.right)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0]

    @CP
    def rules(cls):
        cls._traverse = True
        r = cls.rule
        cls._traverse = False
        return [r]

    _traverse = False

    _active = True

    @classmethod
    def rules_count(cls):
        return len(cls.rules)

    @classmethod
    def count(cls):
        return cls.rules_count()
