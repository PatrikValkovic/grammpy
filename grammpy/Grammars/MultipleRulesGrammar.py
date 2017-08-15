#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.08.2017 14:40
:Licence GNUv3
Part of grammpy

"""

from .StringGrammar import StringGrammar
from ..HashContainer import HashContainer
from ..IsMethodsRuleExtension import IsMethodsRuleExtension as Rule

count = 0


class MultipleRulesGrammar(StringGrammar):
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        super().__init__(terminals, nonterminals, rules, start_symbol)

    def _create_class(self, rule):
        return type('SplitRules' + str(count),
                    (Rule,),
                    {"rule": rule})

    def _transform_rules(self, rules):
        rules = HashContainer.to_iterable(rules)
        r = []
        for i in rules:
            if i.is_valid() and i.count() > 1:
                for rule in i.rules:
                    r.append(self._create_class(rule))
            else:
                r.append(i)
        return rules

    def get_rule(self, rules=None):
        if rules is None:
            return super().get_rule()
        results = super().get_rule(self._transform_rules(rules))
        if not HashContainer.is_iterable(rules):
            return results[0]
        return results

    def have_rule(self, rules):
        return super().have_rule(self._transform_rules(rules))

    def remove_rule(self, rules=None):
        if rules is None:
            return super().remove_rule()
        super().remove_rule(self._transform_rules(rules))

    def add_rule(self, rules):
        super().add_rule(self._transform_rules(rules))
