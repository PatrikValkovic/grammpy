#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 19:25
:Licence GNUv3
Part of grammpy

"""

from .RulesRemovingGrammar import RulesRemovingGrammar as _G


class Grammar(_G):
    def __copy__(self):
        return Grammar(terminals=(t.s for t in self.terms()),
                       nonterminals=self.nonterms(),
                       rules=self.rules(),
                       start_symbol=self.start_get())
