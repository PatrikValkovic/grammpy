#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence GPLv3
Part of grammpy

"""
import inspect
from typing import Iterable, List, TYPE_CHECKING, Type, Generator, Optional

from .SplitRule import SplitRule
from .. import Rule
from ...exceptions import NotRuleException, NonterminalDoesNotExistsException, TerminalDoesNotExistsException

if TYPE_CHECKING:  # pragma: no-cover
    from .. import Grammar


class _RulesSet(set):
    """
    Set that store terminals inside the grammar.
    TODO: implement rest of modify methods.
    """

    def __init__(self, grammar, assign_map, iterable=None):
        # type: (Grammar, dict, Iterable[Type[Rule]]) -> None
        """
        Create new instance of _RulesSet.
        :param grammar: Grammar for which create the set.
        :param assign_map: Map used for assignment rules to terminals or nonterminals.
        This map will be used for deleting rules with terminals or nonterminals within.
        :param iterable: Terminals to insert.
        """
        self._grammar = grammar
        self._assign_map = assign_map
        super().__init__()
        self.add(*(iterable or []))

    def _validate_rule(self, rule):
        # type: (Type[Rule]) -> None
        """
        Validate rule. Valid rule must inherit from Rule and have valid syntax.
        :param rule: Rule to validate.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        """
        if not inspect.isclass(rule) or not issubclass(rule, Rule):
            raise NotRuleException(rule)
        rule.validate(self._grammar)

    def _split_rules(self, original_rule):
        # type: (Type[Rule]) -> Iterable[Type[Rule]]
        """
        Splits Rule class with multiple rules into separate classes, each with only one rule defined.
        The created rules inherits from SplitRule.
        If parameter define only one rule, its not split.
        :param original_rule: Rule to split.
        :return: Iterable of rules derived from the parameter.
        """
        if original_rule.count == 1:
            return [original_rule]

        def yielding(original_rule):
            for rule_index in range(original_rule.count):
                yield SplitRule._create_class(original_rule, rule_index)

        return yielding(original_rule)

    def add(self, *rules):
        # type: (Iterable[Type[Rule]]) -> List[Type[Rule]]
        """
        Add rules into the set. Each rule is validated and split if needed.
        :param rules: Rules to insert.
        :return: Inserted rules.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        :raise RuleException: If the syntax of the rule is invalid.
        """
        return list(self._add(*rules))

    def _add(self, *rules):
        # type: (Iterable[Type[Rule]]) -> Generator[Type[Rule]]
        """
        Add rules into the set. Each rule is validated and split if needed.
        The method add the rules into dictionary, so the rule can be deleted with terminals or nonterminals.
        :param rules: Rules to insert.
        :return: Inserted rules.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        :raise RuleException: If the syntax of the rule is invalid.
        """
        for rule in rules:
            if rule in self:
                continue
            self._validate_rule(rule)
        for rule in rules:
            for r in self._split_rules(rule):
                for side in r.rule:
                    for s in side:
                        self._assign_map[s].add(r)
                super().add(r)
                yield r

    def remove(self, *rules, _validate=True):
        # type: (Iterable[Type[Rule]], bool) -> None
        """
        Remove rules from the set.
        :param rules: Rules to remove.
        :param _validate: True if the rule should be validated before deleting.
        This parameter is only for internal use.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        :raise RuleException: If the syntax of the rule is invalid.
        """
        for rule in rules:
            if rule not in self:
                continue
            if _validate:
                self._validate_rule(rule)
            for r in self._split_rules(rule):
                if r not in self:
                    continue
                for side in r.rule:
                    for s in side:
                        self._assign_map[s].discard(r)
                super().remove(r)

    def __contains__(self, o):
        # type: (Type[Rule]) -> bool
        """
        Check, if is rule in the set.
        :param o: Rule to check.
        :return: True if the rule is in the set, false otherwise.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        :raise RuleException: If the syntax of the rule is invalid.
        """
        try:
            self._validate_rule(o)
            for r in self._split_rules(o):
                if not super().__contains__(r):
                    return False
            return True
        except (TerminalDoesNotExistsException, NonterminalDoesNotExistsException):
            return False

    def get(self, *rules):
        # type: (Iterable[Type[Rule]]) -> List[Type[Rule]]
        """
        Get rules representing parameters.
        The return rules can be different from parameters, in case parameter define multiple rules in one class.
        :param rules: For which rules get the representation.
        :return: List of rules representing parameters.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        :raise RuleException: If the syntax of the rule is invalid.
        """
        return list(self._get(*rules))

    def _get(self, *rules):
        # type: (Iterable[Type[Rule]]) -> Generator[Type[Rule]]
        """
        Get rules representing parameters.
        The return rules can be different from parameters, in case parameter define multiple rules in one class.
        :param rules: For which rules get the representation.
        :return: List of rules representing parameters.
        :raise NotRuleException: If the parameter doesn't inherit from Rule.
        :raise RuleException: If the syntax of the rule is invalid.
        """
        for rule in rules:
            if not inspect.isclass(rule) or not issubclass(rule, Rule):
                raise NotRuleException(rule)
            for r in self._split_rules(rule):
                yield self._find_rule(r)

    def _find_rule(self, rule):
        # type: (Type[Rule]) -> Optional[Type[Rule]]
        """
        Find rule representing parameter.
        :param rule: Rule to find.
        :return: Rule stored inside the set.
        TODO replace with hash?
        """
        for r in self:
            if r == rule:
                return r
        return None
