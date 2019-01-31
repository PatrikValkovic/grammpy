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


class _MetaRule(type):
    """
    Metaclass for rule
    """

    def __init__(cls, name, bases, dct):
        cls._traverse = False
        super(_MetaRule, cls).__init__(name, bases, dct)

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

    @staticmethod
    def _get_toSymbol(cls):
        # type: (_MetaRule) -> object
        if cls._traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        right = cls.rules[0][1]
        if len(right) > 1:
            raise NotASingleSymbolException(right)
        return right[0]

    @staticmethod
    def _get_fromSymbol(cls):
        if cls._traverse:
            raise RuleNotDefinedException(cls)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        left = cls.rules[0][0]
        if len(left) > 1:
            raise NotASingleSymbolException(left)
        return left[0]

    @staticmethod
    def _get_right(cls):
        if cls._traverse:
            return [cls.toSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][1]

    @staticmethod
    def _get_left(cls):
        if cls._traverse:
            return [cls.fromSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][0]

    @staticmethod
    def _get_rule(cls):
        if cls._traverse:
            return (cls.left, cls.right)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0]

    @staticmethod
    def _get_rules(cls):
        cls._traverse = True
        r = cls.rule
        cls._traverse = False
        return [r]

    def __getattr__(cls, name):
        # type: (_MetaRule, str) -> Any
        if name in {'toSymbol',
                    'fromSymbol',
                    'left',
                    'right',
                    'rule',
                    'rules'}:
            return getattr(_MetaRule, '_get_' + name)(cls)
        return super().__getattr__(name)

    @property
    def count(cls):
        """
        Get count of rules defined in the class
        :return: Count of rules
        """
        return len(cls.rules)

    @property
    def rules_count(cls):
        """
        Get count of rules defined in the class
        :return: Count of rules
        """
        return cls.count

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
            cls._controlSide(l, grammar)
            cls._controlSide(r, grammar)
            if l == [EPS] and r == [EPS]:
                raise UselessEpsilonException(cls)

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

    def __getattr__(self, name):
        if name in {'toSymbol',
                    'fromSymbol',
                    'left',
                    'right',
                    'rule',
                    'rules'}:
            return getattr(self.__class__, name)
        return super().__getattr__(name)

    def __hash__(self) -> int:
        return hash(self.__class__)

    def __eq__(self, o: object) -> bool:
        return hash(self) == hash(o)

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
