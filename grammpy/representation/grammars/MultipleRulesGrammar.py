#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.08.2017 14:40
:Licence GNUv3
Part of grammpy

"""
import inspect

from grammpy import Rule
from .StringGrammar import StringGrammar
from grammpy.representation.HashContainer import HashContainer


class SplitRule(Rule):
    from_rule = None
    rule_index = None
    rule = None


class MultipleRulesGrammar(StringGrammar):
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        self._count = 0
        super().__init__(terminals, nonterminals, rules, start_symbol)

    def _create_class(self, rule):
        name = 'SplitRules' + str(self._count)
        self._count += 1
        created = type(name, (SplitRule,), SplitRule.__dict__.copy())
        created.rule = rule
        return created

    def _transform_rules(self, rules, *, _validate=True):
        rules = HashContainer.to_iterable(rules)
        r = []
        for i in rules:
            if not inspect.isclass(i) or not issubclass(i, Rule):
                r.append(i)
            elif (i.is_valid(self) and i.count() > 1) or (not _validate and i.count() > 1):
                for rule_index in range(len(i.rules)):
                    rule = i.rules[rule_index]
                    created = self._create_class(rule)
                    created.from_rule = i
                    created.rule_index = rule_index
                    r.append(created)
            else:
                r.append(i)
        return r

    def get_rule(self, rules=None):
        if rules is None:
            return super().get_rule()
        results = super().get_rule(self._transform_rules(rules))
        if not HashContainer.is_iterable(rules) and rules.count() == 1:
            return results[0]
        return results

    def have_rule(self, rules):
        return super().have_rule(self._transform_rules(rules))

    def remove_rule(self, rules=None, *, _validate=True):
        if rules is None:
            return super().remove_rule(_validate=_validate)
        return super().remove_rule(self._transform_rules(rules, _validate=_validate), _validate=_validate)

    def add_rule(self, rules):
        return super().add_rule(self._transform_rules(rules))
