#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 17:28
:Licence GNUv3
Part of grammpy

"""

from .PrettyApiGrammar import PrettyApiGrammar
from ..constants import EPSILON

class RulesRemovingGrammar(PrettyApiGrammar):
    """
    Class that automatically removing rules, when terminal or nonterminals is removed and there exists rules using that symbol
    """
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        __doc__ = PrettyApiGrammar.__init__.__doc__
        self._symbs_of_rules = dict({EPSILON: set()})
        super().__init__(terminals, nonterminals, rules, start_symbol)

    def add_rule(self, rules):
        #   __doc__ = PrettyApiGrammar.add_rule.__doc__
        add = super().add_rule(rules)
        for inst in add:
            for rule in inst.rules:
                for symb in rule[0]:
                    self._symbs_of_rules[symb].add(inst)
                for symb in rule[1]:
                    self._symbs_of_rules[symb].add(inst)
        return add

    def _remove_if_exists(self, nonterminal, rule):
        """
        Remove rule from the inner database
        :param nonterminal: Nonterminal for which delete the record
        :param rule: Deleting rule
        """
        if rule in self._symbs_of_rules[nonterminal]:
            self._symbs_of_rules[nonterminal].remove(rule)

    def remove_rule(self, rules=None, *, _validate=True):
        __doc__ = PrettyApiGrammar.remove_rule.__doc__
        rem = super().remove_rule(rules, _validate=_validate)
        for inst in rem:
            for rule in inst.rules:
                for side in rule:
                    for symb in side:
                        self._remove_if_exists(symb, inst)
        return rem
