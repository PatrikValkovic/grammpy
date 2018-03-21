#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""

from .MultipleRulesGrammar import MultipleRulesGrammar


class PrettyApiGrammar(MultipleRulesGrammar):

    # Start symbol
    def start_isSet(self):
        return self.start_get() is not None

    def start_is(self, nonterminal):
        return self.start_get() is nonterminal

    # Rules
    def rule(self, rules=None):
        return self.get_rule(rules)

    def rules(self):
        return self.rule()

    def rules_count(self):
        return len(self.rules())

    # Nonterminals
    def nonterm(self, nonterms=None):
        return self.get_nonterm(nonterms)

    def nonterms(self):
        return self.nonterm()

    def nonterms_count(self):
        return len(self.nonterms())

    # Terminals
    def term(self, term=None):
        return self.get_term(term)

    def terms(self):
        return self.term()

    def terms_count(self):
        return len(self.terms())
