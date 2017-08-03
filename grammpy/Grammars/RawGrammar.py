#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
import inspect
from grammpy.Terminal import Terminal
from grammpy.Nonterminal import Nonterminal
from grammpy.HashContainer import HashContainer
from grammpy.exceptions import NotNonterminalException


class RawGrammar:
    def __init__(self, terminals=None, nonterminals=None, rules=None):
        terminals = [] if terminals is None else terminals
        nonterminals = [] if nonterminals is None else nonterminals
        rules = [] if rules is None else rules
        # TODO fill and add tests
        self.__terminals = HashContainer(terminals)
        self.__nonterminals = HashContainer(nonterminals)

    # Term part
    def add_term(self, term):
        return self.__terminals.add(term)

    def remove_term(self, term=None):
        return self.__terminals.remove(term)

    def have_term(self, term):
        return self.__terminals.have(term)

    def get_term(self, term=None):
        if term is not None and not HashContainer.is_iterable(term):
            item = self.__terminals.get(term)
            return Terminal(item, self) if item is not None else None
        vals = []
        obtain = self.__terminals.get(term)
        for t in obtain:
            vals.append(Terminal(t, self) if t is not None else None)
        return vals

    def term(self, term=None):
        return self.get_term(term)

    def terms(self):
        return [Terminal(term,self) for term in self.__terminals.all()]


    def terms_count(self):
        return self.__terminals.count()

    # Non term part
    @staticmethod
    def __controll_nonterms(nonterms):
        nonterms = HashContainer.to_iterable(nonterms)
        for nonterm in nonterms:
            if not inspect.isclass(nonterm) or not issubclass(nonterm, Nonterminal):
                raise NotNonterminalException(nonterm)
        return nonterms

    def add_nonterm(self, nonterms):
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.add(nonterms)

    def remove_nonterm(self, nonterms=None):
        if nonterms is None:
            return self.__nonterminals.remove()
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.remove(nonterms)

    def have_nonterm(self, nonterms):
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.have(nonterms)

    def get_nonterm(self, nonterms=None):
        if nonterms is None:
            return self.__nonterminals.get()
        converted = RawGrammar.__controll_nonterms(nonterms)
        if not HashContainer.is_iterable(nonterms):
            return self.__nonterminals.get(converted)[0]
        return self.__nonterminals.get(converted)

    def nonterm(self, nonterms=None):
        return self.get_nonterm(nonterms)

    def nonterms(self):
        return self.__nonterminals.get()

    def nonterms_count(self):
        return self.__nonterminals.count()

    # Rules part
    def add_rule(self, rules):
        raise NotImplementedError()

    def remove_rule(self, nonterms=None):
        raise NotImplementedError()

    def have_rule(self, nonterms):
        raise NotImplementedError()

    def get_rule(self, nonterms=None):
        raise NotImplementedError()

    def rule(self, nonterms=None):
        raise NotImplementedError()

    def rules(self):
        raise NotImplementedError()

    def rules_count(self):
        raise NotImplementedError()
