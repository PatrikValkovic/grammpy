#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.08.2017 14:40
:Licence GNUv3
Part of grammpy

"""

from .StringGrammar import StringGrammar


class MultipleRulesGrammar(StringGrammar):
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        super().__init__(terminals, nonterminals, rules, start_symbol)

    def get_rule(self, rules=None):
        return super().get_rule(rules)

    def have_rule(self, rules):
        return super().have_rule(rules)

    def remove_rule(self, rules=None):
        super().remove_rule(rules)

    def add_rule(self, rules):
        super().add_rule(rules)
