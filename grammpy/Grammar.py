#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
import types
import collections


class Grammar:
    def __init__(self, terminals=None, nonterminals=None, rules=None):
        # Ensure that parameters are immutable
        if rules is None:
            rules = []
        if nonterminals is None:
            nonterminals = []
        if terminals is None:
            terminals = []
        # TODO fill and add tests
        self.__terminals = {}
        self.__nonterminals = {}

    # Helpers
    def __to_iterable(self, param):
        # standardize it to iterable object
        if isinstance(param, types.StringTypes) or not isinstance(param, collections.Iterable):
            return (param,)
        return param

    # Term part
    def add_term(self, term):
        term = self.__to_iterable(term)
        # iterace throught items
        for t in term:
            self.__terminals[hash(t)] = t

    def remove_term(self, term=None):
        if term is None:
            return self.__terminals.clear()
        term = self.__to_iterable(term)
        # iterace throught items
        for t in term:
            self.__terminals[hash(t)] = t

    def have_term(self, term):
        # TODO add test for term as array
        term = self.__to_iterable(term)
        for t in term:
            if not self.__terminals.has_key(hash(t)):
                return False
        return True

    def get_term(self, term):
        # TODO add test for them as array
        transformed = self.__to_iterable(term)
        #TODO
        raise NotImplementedError()

    def term(self, term):
        return self.get_term(term)

    def terms(self):
        return [item for item, _ in self.__terminals]

    def terms_count(self):
        return len(self.__terminals)

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
