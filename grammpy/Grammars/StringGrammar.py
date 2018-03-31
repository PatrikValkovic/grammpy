#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""

from .RawGrammar import RawGrammar

class StringGrammar(RawGrammar):
    def __init__(self, terminals=None, nonterminals=None, rules=None, start_symbol=None):
        if isinstance(terminals, str):
            terminals = [t for t in terminals]
        super().__init__(terminals, nonterminals, rules, start_symbol)

    @staticmethod
    def __to_string_arr(t):
        if isinstance(t, str):
            return [t]
        return t

    def remove_term(self, term=None):
        return super().remove_term(StringGrammar.__to_string_arr(term))

    def add_term(self, term):
        return super().add_term(StringGrammar.__to_string_arr(term))

    def get_term(self, term=None):
        res = super().get_term(StringGrammar.__to_string_arr(term))
        if isinstance(term, str):
            return res[0]
        return res

    def have_term(self, term):
        return super().have_term(StringGrammar.__to_string_arr(term))
