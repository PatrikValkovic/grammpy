#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 19:25
:Licence GNUv3
Part of grammpy

"""

from .CopyableGrammar import CopyableGrammar



class Grammar(CopyableGrammar):
    def __copy__(self):
        return self.copy()

    def copy(self, terminals=False, nonterminals=False, rules=False):
        c = self._copy(terminals=terminals, nonterminals=nonterminals, rules=rules)
        return Grammar(terminals=list(c.new_terms),
                       nonterminals=list(c.new_nonterms),
                       rules=list(c.new_rules),
                       start_symbol=c.start)

    def __deepcopy__(self, memodict={}):
        return self.copy(terminals=True, nonterminals=True, rules=True)
