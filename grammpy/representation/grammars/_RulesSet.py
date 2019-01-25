#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence GPLv3
Part of grammpy

"""
import inspect
from typing import Iterable, List, TYPE_CHECKING, Type, Generator

from .. import Rule
from ..rules.support import SplitRule
from ...exceptions import NotRuleException, NonterminalDoesNotExistsException, TerminalDoesNotExistsException

if TYPE_CHECKING:
    from ..grammars import Grammar


class _RulesSet(set):
    def __init__(self, grammar, assign_map, iterable=None):
        # type: (Grammar, dict, Iterable[Type[Rule]]) -> None
        self._grammar = grammar
        self._assign_map = assign_map
        super().__init__()
        iterable = [] if iterable is None else iterable
        self.add(*iterable)

    def _validate_rule(self, rule):
        # type: (Type[Rule]) -> None
        if not inspect.isclass(rule) or not issubclass(rule, Rule):
            raise NotRuleException(rule)
        rule.validate(self._grammar)

    def _split_rules(self, original_rule):
        # type: (Type[Rule]) -> Iterable[Type[Rule]]
        if original_rule.count() == 1:
            return [original_rule]

        def yielding(original_rule):
            for rule_index in range(original_rule.count()):
                yield SplitRule._create_class(original_rule, rule_index)

        return yielding(original_rule)

    def add(self, *rules):
        return list(self._add(*rules))

    def _add(self, *rules):
        # type: (Iterable[Type[Rule]]) -> Generator[Type[Rule]]
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
        return list(self._get(*rules))

    def _get(self, *rules):
        # type: (Iterable[Type[Rule]]) -> Generator[Type[Rule]]
        for rule in rules:
            if not inspect.isclass(rule) or not issubclass(rule, Rule):
                raise NotRuleException(rule)
            for r in self._split_rules(rule):
                yield self._find_rule(r)

    def _find_rule(self, rule):
        for r in self:
            if r == rule:
                return r
        return None
