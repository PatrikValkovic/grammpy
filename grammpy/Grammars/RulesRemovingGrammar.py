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
        self._symbs_of_rules = dict()
        super().__init__(terminals, nonterminals, rules, start_symbol)

    def add_term(self, term):
        add = super().add_term(term)
        for t in add: self._symbs_of_rules[t.s] = set()
        return add

    def remove_term(self, term=None):
        rem = super().remove_term(term)
        for term in rem:
            self.remove_rule(list(self._symbs_of_rules[term.s]), _validate=False)
            del self._symbs_of_rules[term.s]
        return rem

    def add_nonterm(self, nonterms):
        add = super().add_nonterm(nonterms)
        for n in add: self._symbs_of_rules[n] = set()
        return add

    def remove_nonterm(self, nonterms=None):
        rem = super().remove_nonterm(nonterms)
        for nonterm in rem:
            self.remove_rule(list(self._symbs_of_rules[nonterm]), _validate=False)
            del self._symbs_of_rules[nonterm]
        if self.start_get() in rem: self.start_set(None)
        return rem

    def add_rule(self, rules):
        add = super().add_rule(rules)
        for inst in add:
            for rule in inst.rules:
                for symb in rule[0]:
                    self._symbs_of_rules[symb].add(inst)
                for symb in rule[1]:
                    self._symbs_of_rules[symb].add(inst)
        return add

    def _remove_if_exists(self, key, val):
        if val in self._symbs_of_rules[key]:
            self._symbs_of_rules[key].remove(val)

    def remove_rule(self, rules=None, *, _validate=True):
        rem = super().remove_rule(rules, _validate=_validate)
        for inst in rem:
            for rule in inst.rules:
                for side in rule:
                    for symb in side:
                        self._remove_if_exists(symb, inst)
        return rem
