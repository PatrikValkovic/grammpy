#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
import inspect
from ..Terminal import Terminal
from ..Nonterminal import Nonterminal
from ..HashContainer import HashContainer
from ..exceptions import NotNonterminalException, NotRuleException, TerminalDoesNotExistsException, NonterminalDoesNotExistsException
from ..IsMethodsRuleExtension import IsMethodsRuleExtension


class RawGrammar:
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol = None):
        terminals = [] if terminals is None else terminals
        nonterminals = [] if nonterminals is None else nonterminals
        rules = [] if rules is None else rules
        self.__terminals = HashContainer()
        self.__nonterminals = HashContainer()
        self.__rules = HashContainer()
        self.add_term(terminals)
        self.add_nonterm(nonterminals)
        self.add_rule(rules)
        #TODO start symbol

    # Term part
    # TODO add validation of terminals that no rule or nonterminal is passed
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
        return [Terminal(term, self) for term in self.__terminals.all()]

    def terms_count(self):
        return self.__terminals.count()

    # Non term part
    @staticmethod
    def _controll_nonterms(nonterms):
        nonterms = HashContainer.to_iterable(nonterms)
        for nonterm in nonterms:
            if not inspect.isclass(nonterm) or not issubclass(nonterm, Nonterminal):
                raise NotNonterminalException(nonterm)
        return nonterms

    def add_nonterm(self, nonterms):
        nonterms = RawGrammar._controll_nonterms(nonterms)
        return self.__nonterminals.add(nonterms)

    def remove_nonterm(self, nonterms=None):
        if nonterms is None:
            return self.__nonterminals.remove()
        nonterms = RawGrammar._controll_nonterms(nonterms)
        return self.__nonterminals.remove(nonterms)

    def have_nonterm(self, nonterms):
        nonterms = RawGrammar._controll_nonterms(nonterms)
        return self.__nonterminals.have(nonterms)

    def get_nonterm(self, nonterms=None):
        if nonterms is None:
            return self.__nonterminals.get()
        converted = RawGrammar._controll_nonterms(nonterms)
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
    def _control_rules(self, rules):
        rules = HashContainer.to_iterable(rules)
        for rule in rules:
            if not inspect.isclass(rule) or not issubclass(rule, IsMethodsRuleExtension):
                raise NotRuleException(rule)
            rule.validate(self)
        return rules

    def add_rule(self, rules):
        rules = self._control_rules(rules)
        return self.__rules.add(rules)

    def remove_rule(self, rules=None):
        if rules is None:
            return self.__rules.remove()
        rules = self._control_rules(rules)
        return self.__rules.remove(rules)

    def have_rule(self, rules):
        try:
            rules = self._control_rules(rules)
            return self.__rules.have(rules)
        except (TerminalDoesNotExistsException, NonterminalDoesNotExistsException):
            return False

    def get_rule(self, rules=None):
        if rules is None:
            return [rule for rule in self.__rules.get() if rule._active]
        converted = self._control_rules(rules)
        if not HashContainer.is_iterable(rules):
            return self.__rules.get(converted)[0]
        return self.__rules.get(converted)

    def rule(self, rules=None):
        return self.get_rule(rules)

    def rules(self):
        return self.rule()

    def rules_count(self):
        return len(self.rules())


    #StartSymbol
    def start_get(self):
        raise NotImplementedError()

    def start_set(self, nonterminal):
        raise NotImplementedError()

    def start_isSet(self):
        raise NotImplementedError()

    def start_is(self, nonterminal):
        raise NotImplementedError()
