#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 19:25
:Licence GNUv3
Part of grammpy

"""

from .CopyableGrammar import CopyableGrammar



class Grammar(CopyableGrammar):
    """
    Grammar class that hides underlying classes
    """
    def __copy__(self):
        """
        Create copy of the grammar
        :return: Copy of the current grammar
        """
        return self.copy()

    def copy(self, terminals=False, nonterminals=False, rules=False):
        """
        Copy current grammar
        :param terminals: True if terminals should be deep copied, False by default
        :param nonterminals: True if nonterminals should be deep copied, False by default
        :param rules: True if rules should be deep copied, False by default
        :return: Copied grammar
        """
        c = self._copy(terminals=terminals, nonterminals=nonterminals, rules=rules)
        return Grammar(terminals=list(c.new_terms),
                       nonterminals=list(c.new_nonterms),
                       rules=list(c.new_rules),
                       start_symbol=c.start)

    def __deepcopy__(self, memodict={}):
        """
        Deep copy of the grammar
        :param memodict:
        :return: Deep copy of the current grammar
        """
        return self.copy(terminals=True, nonterminals=True, rules=True)
