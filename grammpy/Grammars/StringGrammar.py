#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from grammpy.Grammars.RawGrammar import RawGrammar as Grammar


class StringGrammar(Grammar):
    @staticmethod
    def __to_string_arr(t):
        if isinstance(t, str):
            return [t]
        return t

    def remove_term(self, term=None):
        return super().remove_term(StringGrammar.__to_string_arr(term))

    def add_term(self, term):
        return super().add_term(StringGrammar.__to_string_arr(term))

    def term(self, term=None):
        return self.get_term(term)

    def get_term(self, term=None):
        res = super().get_term(StringGrammar.__to_string_arr(term))
        if isinstance(term, str):
            return res[0]
        return res

    def have_term(self, term):
        return super().have_term(StringGrammar.__to_string_arr(term))
