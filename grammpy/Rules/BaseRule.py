#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:45
:Licence GNUv3
Part of grammpy

"""
import inspect

from grammpy.exceptions import CantCreateSingleRuleException, RuleNotDefinedException, NotASingleSymbolException


def lists_to_tuples(lst):
    """
    Recursively transforms lists to tuples
    :param lst: List, that can contain another lists
    :return: Tuple
    """
    if not isinstance(lst, list) and not isinstance(lst, tuple):
        return lst
    return tuple(lists_to_tuples(item) for item in tuple(lst))


class CP(object):
    """
    Definition of class property decorator
    """
    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls=None):
        return self._getter(cls)  # for static remove cls from the call

class MetaRule(type):
    """
    Metaclass for rule
    """
    def __hash__(cls):
        """
        Get hash for Rule class
        :return: Hash of the Rule class
        """
        try:
            return cls.ruleHash()
        except RuleNotDefinedException:
            return super(BaseRule, cls).__hash__(cls)

    def __eq__(cls, other):
        """
        Compare two Rule classes
        :param other: Another Rule class
        :return: True if both classes contains same rules, false otherwise
        """
        return inspect.isclass(other) and \
               issubclass(other, BaseRule) and \
               hash(cls) == hash(other)


class BaseRule(metaclass=MetaRule):
    """
    Basic implementation of rules.
    For definition of rule, you can use following attributes:
    fromSymbol = EPSILON
    toSymbol = EPSILON
    left = [EPSILON]
    right = [EPSILON]
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

    @classmethod
    def rules_count(cls):
        """
        Get count of rules defined in the class
        :return: Count of rules
        """
        return len(cls.rules)

    @classmethod
    def count(cls):
        """
        Get count of rules defined in the class
        :return: Count of rules
        """
        return cls.rules_count()

    @classmethod
    def ruleHash(cls):
        """
        Return hash of Rule class
        :return: Hash of the class
        """
        transformed = lists_to_tuples(cls.rules)
        return hash(transformed)
