#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 17:28
:Licence GNUv3
Part of grammpy

"""

from .PrettyApiGrammar import PrettyApiGrammar


class RulesRemovingGrammar(PrettyApiGrammar):
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        super().__init__(terminals, nonterminals, rules, start_symbol)

    def remove_term(self, term=None):
        return super().remove_term(term)

    def remove_nonterm(self, nonterms=None):
        return super().remove_nonterm(nonterms)

    def add_term(self, term):
        return super().add_term(term)

    def add_nonterm(self, nonterms):
        return super().add_nonterm(nonterms)

    def remove_rule(self, rules=None):
        return super().remove_rule(rules)

    def add_rule(self, rules):
        return super().add_rule(rules)
