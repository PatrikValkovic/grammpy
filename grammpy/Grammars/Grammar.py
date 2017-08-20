#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 19:25
:Licence GNUv3
Part of grammpy

"""

from .CopyableGrammar import CopyableGrammar as _G



class Grammar(_G):
    def __copy__(self):
        return self.copy()

    def copy(self, terminals=False, nonterminals=False, rules=False):
        c = self._copy(terminals=terminals, nonterminals=nonterminals, rules=rules)
        return Grammar(terminals=list(c.new_terms),
                       nonterminals=list(c.new_nonterms),
                       rules=list(c.new_rules),
                       start_symbol=c.start)

    def copy_rules(self):
        return self.copy(rules=True)

    def __deepcopy__(self, memodict={}):
        return self.copy(terminals=True, nonterminals=True, rules=True)
