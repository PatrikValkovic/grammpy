#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.01.2019 13:46
:Licence MIT
Part of grammpy

"""

from inspect import isclass
from typing import Any, List, TYPE_CHECKING

from ._constants import EPS
from ..Nonterminal import Nonterminal
from ...exceptions import *

if TYPE_CHECKING:  # pragma: no cover
    from .. import Grammar


class _MetaRule(type):
    """
    Metaclass for rule.
    Contains logic, how to compute toSymbol, fromSymbol, left, right, rule, rules properties.
    Contains logic about rule validation.
    """

    def __init__(cls, name, bases, dct):
        cls._traverse = False
        super(_MetaRule, cls).__init__(name, bases, dct)

    def __hash__(cls):
        # type: (_MetaRule) -> int
        """
        Get hash for Rule class.
        :return: Hash of the Rule class.
        """
        try:
            transformed = tuple((tuple(s for s in rule[0]), tuple(s for s in rule[1])) for rule in cls.rules)
            return hash(transformed)
        except RuleNotDefinedException:
            return super().__hash__()

    def __eq__(cls, other):
        # type: (_MetaRule, object) -> bool
        """
        Compare two Rule classes.
        :param other: Another Rule class.
        :return: True if both classes contains same rules, false otherwise.
        """
        return isclass(other) and hash(cls) == hash(other)

    @staticmethod
    def _get_toSymbol(cls):
        # type: (_MetaRule) -> object
        """
        Get symbol from which the rule is rewrote.
        :param cls: Rule for which return the symbol.
        :return: Symbol from which the rule is rewrote.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
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
        # type: (_MetaRule) -> object
        """
        Get symbol to which the rule is rewrote.
        :param cls: Rule for which return the symbol.
        :return: Symbol to which the rule is rewrote.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the right is more.
        """
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
        # type: (_MetaRule) -> List[object]
        """
        Get right part of the rule.
        :param cls: Rule for which return the right side.
        :return: Symbols on the right side of the array.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
        if cls._traverse:
            return [cls.toSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][1]

    @staticmethod
    def _get_left(cls):
        # type: (_MetaRule) -> List[object]
        """
        Get left part of the rule.
        :param cls: Rule for which return the left side.
        :return: Symbols on the left side of the array.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
        if cls._traverse:
            return [cls.fromSymbol]
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0][0]

    @staticmethod
    def _get_rule(cls):
        # type: (_MetaRule) -> (List[object], List[object])
        """
        Get rule on the Rule class.
        :param cls: Rule for which return the rule.
        :return: Rule inside the Rule class.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
        if cls._traverse:
            return (cls.left, cls.right)
        if len(cls.rules) > 1:
            raise CantCreateSingleRuleException(cls)
        return cls.rules[0]

    @staticmethod
    def _get_rules(cls):
        # type: (_MetaRule) -> List[(List[object], List[object])]
        """
        Get rules on the Rule class.
        :param cls: Rule for which return the rules.
        :return: Rules inside the Rule class.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
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
        raise AttributeError

    @property
    def count(cls):
        # type: (_MetaRule) -> int
        """
        Get count of rules defined in the class.
        :return: Count of rules.
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
        return len(cls.rules)

    @property
    def rules_count(cls):
        # type: (_MetaRule) -> int
        """
        Get count of rules defined in the class
        :return: Count of rules
        :raise RuleNotDefinedException: If the rule is not defined.
        :raise CantCreateSingleRuleException: If the rule consists of more rules.
        :raise NotASingleSymbolException: If number of symbols on the left is more.
        """
        return cls.count

    def _controlSide(cls, side, grammar):
        # type: (_MetaRule, List[object], Grammar) -> None
        """
        Validate one side of the rule.
        :param side: Iterable side of the rule.
        :param grammar: Grammar on which to validate.
        :raise RuleSyntaxException: If invalid syntax is use.
        :raise UselessEpsilonException: If useless epsilon is used.
        :raise TerminalDoesNotExistsException: If terminal does not exists in the grammar.
        :raise NonterminalDoesNotExistsException: If nonterminal does not exists in the grammar.
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
        # type: (_MetaRule, Grammar) -> None
        """
        Perform rules validation of the class.
        :param grammar: Grammar on which to validate.
        :raise RuleSyntaxException: If invalid syntax is used.
        :raise UselessEpsilonException: If epsilon used in rules in useless.
        :raise TerminalDoesNotExistsException: If terminal does not exists in the grammar.
        :raise NonterminalDoesNotExistsException: If nonterminal does not exists in the grammar.
        """
        right = cls.rules
        if not isinstance(right, list):
            raise RuleSyntaxException(cls, 'Rules property is not enclose in list')
        for rule in right:
            if not isinstance(rule, tuple):
                raise RuleSyntaxException(cls, 'One of the rules is not enclose in tuple', rule)
            if len(rule) != 2:
                raise RuleSyntaxException(cls, 'One of the rules does not have define left and right part', rule)
            left = rule[0]
            right = rule[1]
            cls._controlSide(left, grammar)
            cls._controlSide(right, grammar)
            if left == [EPS] and right == [EPS]:
                raise UselessEpsilonException(cls)

    def is_valid(cls, grammar):
        # type: (_MetaRule, Grammar) -> bool
        """
        Check if the rule is correctly defined.
        :param grammar: Grammar on which to validate.
        :return: True if have class correct rules, false otherwise.
        """
        try:
            cls.validate(grammar)
            return True
        except RuleException:
            return False
