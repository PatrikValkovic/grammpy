#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""


class Grammar:
    def __init__(self, terminals=[], nonterminals=[], rules=[]):
        self.__terminals = set()
        self.__nonterminals = set()

    # Term part
    def add_term(self, term):
        raise NotImplementedError()

    def remove_term(self, term=None):
        raise NotImplementedError()

    def have_term(self, term):
        raise NotImplementedError()

    def get_term(self, term):
        raise NotImplementedError()

    def term(self, term):
        raise NotImplementedError()

    def terms(self):
        raise NotImplementedError()

    def terms_count(self):
        raise NotImplementedError()

    # Non term part
    def add_nonterm(self, nonterm):
        raise NotImplementedError()

    def remove_nonterm(self, nonterm=None):
        raise NotImplementedError()

    def have_nonterm(self, nonterm):
        raise NotImplementedError()

    def get_nonterm(self, nonterm):
        raise NotImplementedError()

    def nonterms(self):
        raise NotImplementedError()

    def nonterms_count(self):
        raise NotImplementedError()


    pass
