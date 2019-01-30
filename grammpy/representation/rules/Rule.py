#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:45
:Licence GNUv3
Part of grammpy

"""
from inspect import isclass
from ...exceptions import *
from .. import EPS
from ..WeakList import WeakList
from ..Nonterminal import Nonterminal


class _ClassProperty(object):
    """
    Definition of class property decorator
    """

    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls=None):
        return self._getter(cls)  # for static remove cls from the call


class _MetaRule(type):
    """
    Metaclass for rule
    """

    def __hash__(cls):
        """
        Get hash for Rule class
        :return: Hash of the Rule class
        """
        try:
            transformed = tuple((tuple(s for s in rule[0]), tuple(s for s in rule[1])) for rule in cls.rules)
            return hash(transformed)
        except RuleNotDefinedException:
            return super(Rule, cls).__hash__(cls)

    def __eq__(cls, other):
        """
        Compare two Rule classes
        :param other: Another Rule class
        :return: True if both classes contains same rules, false otherwise
        """
        return isclass(other) and \
               issubclass(other, Rule) and \
               hash(cls) == hash(other)


class Rule(metaclass=_MetaRule):
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

    def __init__(self):
        self._from_symbols = WeakList()
        self._to_symbols = list()

    _traverse = False

    @_ClassProperty
    def toSymbol(cls):
        if cls._traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        right = cls.rules[0][1]
        if len(right) > 1:
            raise NotASingleSymbolException(right)
        return right[0]

    @_ClassProperty
    def fromSymbol(cls):
        if cls._traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        left = cls.rules[0][0]
        if len(left) > 1:
            raise NotASingleSymbolException(left)
        return left[0]

    @_ClassProperty
    def right(cls):
        if cls._traverse:
            return [cls.toSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][1]

    @_ClassProperty
    def left(cls):
        if cls._traverse:
            return [cls.fromSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][0]

    @_ClassProperty
    def rule(cls):
        if cls._traverse:
            return (cls.left, cls.right)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0]

    @_ClassProperty
    def rules(cls):
        cls._traverse = True
        r = cls.rule
        cls._traverse = False
        return [r]

    @_ClassProperty
    def count(cls):
        """
        Get count of rules defined in the class
        :return: Count of rules
        """
        return len(cls.rules)

    @_ClassProperty
    def rules_count(cls):
        """
        Get count of rules defined in the class
        :return: Count of rules
        """
        return cls.count

    def __hash__(self) -> int:
        return hash(self.__class__)

    def __eq__(self, o: object) -> bool:
        return hash(self) == hash(o)

    @staticmethod
    def _controlSide(cls, side, grammar):
        """
        Validate one side of the rule
        :param side: Iterable side of the rule
        :param grammar: Grammar on which to validate
        :raise RuleSyntaxException: If invalid syntax is use
        :raise UselessEpsilonException: If useless epsilon is used
        :raise TerminalDoesNotExistsException: If terminal does not exists in the grammar
        :raise NonterminalDoesNotExistsException: If nonterminal does not exists in the grammar
        """
        if not isinstance(side, list):
            raise RuleSyntaxException(cls, 'One side of rule is not enclose by list', side)
        if len(side) == 0:
            raise RuleSyntaxException(cls, 'One side of rule is not define', side)
        if EPS in side and len(side) > 1:
            raise UselessEpsilonException(cls)
        for symb in side:
            if isclass(symb) and issubclass(symb, Nonterminal):
                if symb not in grammar.nonterminals:
                    raise NonterminalDoesNotExistsException(cls, symb, grammar)
            elif symb is EPS:
                continue
            elif symb not in grammar.terminals:
                raise TerminalDoesNotExistsException(cls, symb, grammar)

    @classmethod
    def validate(cls, grammar):
        """
        Perform rules validation of the class
        :param grammar: Grammar on which to validate
        :raise RuleSyntaxException: If invalid syntax is used
        :raise UselessEpsilonException: If epsilon used in rules in useless
        :raise TerminalDoesNotExistsException: If terminal does not exists in the grammar
        :raise NonterminalDoesNotExistsException: If nonterminal does not exists in the grammar
        """
        r = cls.rules
        if not isinstance(r, list):
            raise RuleSyntaxException(cls, 'Rules property is not enclose in list')
        for rule in r:
            if not isinstance(rule, tuple):
                raise RuleSyntaxException(cls, 'One of the rules is not enclose in tuple', rule)
            if len(rule) != 2:
                raise RuleSyntaxException(cls, 'One of the rules does not have define left and right part', rule)
            l = rule[0]
            r = rule[1]
            Rule._controlSide(cls, l, grammar)
            Rule._controlSide(cls, r, grammar)
            if l == [EPS] and r == [EPS]:
                raise UselessEpsilonException(cls)

    @classmethod
    def is_valid(cls, grammar):
        """
        Check if are rules correctly defined
        :param grammar: Grammar on which to validate
        :return: True if have class correct rules, false otherwise
        """
        try:
            cls.validate(grammar)
            return True
        except RuleException:
            return False

    @property
    def from_symbols(self):
        """
        Instances of the left side of the rule
        :return: List of symbols
        """
        return list(self._from_symbols)

    @property
    def to_symbols(self):
        """
        Instances of the right side of the rule
        :return: List of symbols
        """
        return self._to_symbols
