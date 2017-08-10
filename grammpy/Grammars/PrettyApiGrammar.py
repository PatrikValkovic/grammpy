#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""

from grammpy.Grammars.StringGrammar import StringGrammar as Grammar


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
