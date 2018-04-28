#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""

from .RawGrammar import RawGrammar

class StringGrammar(RawGrammar):
    """
    Class that proccess string terminal as single terminal, although string is sequence of characters
    """
    def __init__(self, terminals=None, nonterminals=None, rules=None, start_symbol=None):
        __doc__ = RawGrammar.__init__.__doc__
        if isinstance(terminals, str):
            terminals = [t for t in terminals]
        super().__init__(terminals, nonterminals, rules, start_symbol)

    @staticmethod
    def __to_string_arr(t):
        """
        Check if parameter is string and if yes, transform it into list of parameter
        :param t: Object to check
        :return: List containing parameter if parameter is string, original parameter otherwise
        """
        if isinstance(t, str):
            return [t]
        return t

    def remove_term(self, term=None):
        __doc__ = RawGrammar.remove_term.__doc__
        return super().remove_term(StringGrammar.__to_string_arr(term))

    def add_term(self, term):
        __doc__ = RawGrammar.add_term.__doc__
        return super().add_term(StringGrammar.__to_string_arr(term))

    def get_term(self, term=None):
        __doc__ = RawGrammar.get_term.__doc__
        res = super().get_term(StringGrammar.__to_string_arr(term))
        if isinstance(term, str):
            return res[0]
        return res

    def have_term(self, term):
        __doc__ = RawGrammar.have_term.__doc__
        return super().have_term(StringGrammar.__to_string_arr(term))
