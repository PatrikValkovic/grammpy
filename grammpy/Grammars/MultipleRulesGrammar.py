#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.08.2017 14:40
:Licence GNUv3
Part of grammpy

"""
import inspect

from ..Rules import Rule
from .StringGrammar import StringGrammar
from ..HashContainer import HashContainer


class MultipleRulesGrammar(StringGrammar):
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        super().__init__(terminals, nonterminals, rules, start_symbol)
        self._count = 0

    def _create_class(self, rule):
        name = 'SplitRules' + str(self._count)
        self._count += 1
        return type(name,
                    (Rule,),
                    {"rule": rule})

    def _transform_rules(self, rules, *, _validate=True):
        rules = HashContainer.to_iterable(rules)
        r = []
        for i in rules:
            if not inspect.isclass(i) or not issubclass(i, Rule):
                r.append(i)
            elif (i.is_valid(self) and i.count() > 1) or (not _validate and i.count() > 1):
                for rule in i.rules:
                    r.append(self._create_class(rule))
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
