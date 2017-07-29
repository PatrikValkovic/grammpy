#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .StringGrammar import StringGrammar as Grammar


class PrettyApiGrammar(Grammar):
    def __init__(self, terminals=None, nonterminals=None, rules=None):
        if isinstance(terminals, str):
            temp = []
            for ch in terminals:
                temp.append(ch)
            terminals = temp
        super().__init__(terminals=terminals,
                         nonterminals=nonterminals,
                         rules=rules)
