#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 28.08.2017 10:19
:Licence MIT
Part of grammpy

"""
from copy import copy
from queue import Queue
from typing import Any, Type

from ... import *


class ChomskyNonterminal(Nonterminal):
    """
    Base class for all nonterminals used in Chomsky Normal Form.
    """
    pass


class ChomskyGroupNonterminal(ChomskyNonterminal):
    """
    Class representing nonterminal that represents nonterminal tail when rule is splitted.
    """
    group = []


class ChomskyTermNonterminal(ChomskyNonterminal):
    """
    Class representing nonterminal directly rewritable to terminal.
    """
    for_term = None


class ChomskyRule(Rule):
    """
    Base class for all rules used in Chomsky Normal Form.
    """
    pass


class ChomskySplitRule(ChomskyRule):
    """
    Class representing split rule with more than two nonterminals.
    First symbol of the right side is first symbol in the original rule.
    Second symbol of the right side is always ChomskyGroupNonterminal.
    Rule from the ChomskyGroupNonterminal is always ChomskyRestRule.
    """
    from_rule = None


class ChomskyRestRule(ChomskyRule):
    """
    Class representing rule for ChomskyGroupNonterminal class.
    Always rewrote from ChomskyGroupNonterminal.
    """
    from_rule = None


class ChomskyTerminalReplaceRule(ChomskyRule):
    """
    Replacement of rule, that have two symbol on the right side, but one of it is terminal.
    """
    from_rule = None
    replaced_index = None


class ChomskyTermRule(ChomskyRule):
    """
    Rule that directly rewrite nonterminal to terminal.
    """
    pass


class Container:
    """
    Represent container that hold terminal, appropriate ChomskyTermNonterminal for which exists rule
    to rewrite to that terminal and ChomskyTermRule, that rewrites the nonterminal to terminal.
    Purpose of this class is to keep them together.
    """

    def __init__(self, terminal, nonterminal, rule):
        # type: (Any, Type[ChomskyTermNonterminal], Type[ChomskyTermRule]) -> None
        """
        Create instance of the container.
        :param terminal: Original terminal.
        :param nonterminal: Nonterminal directly rewritable to terminal.
        :param rule: Rule that rewrite nonterminal to terminal.
        """
        self.used = False
        self.terminal = terminal
        self.nonterminal = nonterminal
        self.rule = rule


class TerminalsFilling:
    """
    Store all terminals and their appropriate ChomskyTermNonterminal and ChomskyTermRule.
    Automatically add rule and nonterminal into grammar if the rule is used.
    """

    def __init__(self, grammar):
        # type: (Grammar) -> None
        """
        :param grammar: Grammar to work with. Can be modified.
        """
        self._grammar = grammar
        self._items = dict()
        for term in grammar.terminals:
            created_nonterm = type("ChomskyTerm[" + str(term) + "]",
                                   (ChomskyTermNonterminal,),
                                   ChomskyTermNonterminal.__dict__.copy())  # type: Type[ChomskyTermNonterminal]
            created_nonterm.for_term = term
            created_rule = type("ChomskyTerm[" + str(term) + "]",
                                (ChomskyTermRule,),
                                ChomskyTermRule.__dict__.copy())  # type: Type[ChomskyTermRule]
            created_rule.rule = ([created_nonterm], [term])
            self._items[term] = Container(term, created_nonterm, created_rule)

    def get(self, term):
        # type: (Any) -> Type[ChomskyTermNonterminal]
        """
        Get nonterminal rewritable to term.
        If the rules is not in the grammar, nonterminal and rule rewritable to terminal are add into grammar.
        :param term: Term for which get the nonterminal.
        :return: ChomskyTermNonterminal class for terminal.
        """
        if self._items[term].used is False:
            cont = self._items[term]
            self._grammar.nonterminals.add(cont.nonterminal)
            self._grammar.rules.add(cont.rule)
            cont.used = True
        return self._items[term].nonterminal


def transform_to_chomsky_normal_form(grammar, inplace=False):
    # type: (Grammar, bool) -> Grammar
    """
    Transform grammar to Chomsky Normal Form.
    :param grammar: Grammar to transform.
    :param inplace: True if transformation should be performed in place. False by default.
    :return: Grammar in Chomsky Normal Form.
    """
    # Copy if required
    if inplace is False:
        grammar = copy(grammar)
    # Create nonterminals rewritable to the terminal.
    # They will be inserted into the grammar as needed.
    fill = TerminalsFilling(grammar)
    to_process = Queue()
    for r in grammar.rules:
        to_process.put(r)
    while not to_process.empty():
        rule = to_process.get()  # type: Type[Rule]
        # Check, if rule must be split
        if len(rule.right) > 2:
            grammar.rules.remove(rule)
            # create nonterm that represent group on the right
            created_nonterm = type("ChomskyGroup[" + rule.__name__ + "]",
                                   (ChomskyGroupNonterminal,),
                                   ChomskyGroupNonterminal.__dict__.copy())  # type: Type[ChomskyGroupNonterminal]
            created_nonterm.group = rule.right[1:]
            # create rule that replace current
            created_left_rule = type("ChomskySplit[" + rule.__name__ + "]",
                                     (ChomskySplitRule,),
                                     ChomskySplitRule.__dict__.copy())  # type: Type[ChomskySplitRule]
            created_left_rule.rule = ([rule.fromSymbol], [rule.right[0], created_nonterm])
            created_left_rule.from_rule = rule
            # create rule with symbols on the right
            created_right_rule = type("ChomskyRest[" + rule.__name__ + "]",
                                      (ChomskyRestRule,),
                                      ChomskyRestRule.__dict__.copy())  # type: Type[ChomskyRestRule]
            created_right_rule.rule = ([created_nonterm], rule.right[1:])
            created_right_rule.from_rule = rule
            # add it to the grammar
            grammar.nonterminals.add(created_nonterm)
            grammar.rules.add(created_left_rule, created_right_rule)
            to_process.put(created_left_rule)
            to_process.put(created_right_rule)
        # check, if must replace terminal
        elif len(rule.right) == 2:
            if rule.right[0] in grammar.terminals:
                # first symbol is terminal
                # remove rule from grammar
                grammar.rules.remove(rule)
                # get nonterminal rewritable to the terminal and add that rules into the grammar implicitly
                symb = fill.get(rule.right[0])
                # create rule replacing the original one
                created = type("ChomskyLeft[" + rule.__name__ + "]",
                               (ChomskyTerminalReplaceRule,),
                               ChomskyTerminalReplaceRule.__dict__.copy())  # type: Type[ChomskyTerminalReplaceRule]
                created.rule = ([rule.fromSymbol], [symb, rule.right[1]])
                created.from_rule = rule
                created.replaced_index = 0
                # add it into the grammar
                grammar.rules.add(created)
                to_process.put(created)
            elif rule.right[1] in grammar.terminals:
                # second symbol is terminal
                # remove rule from grammar
                grammar.rules.remove(rule)
                # get nonterminal rewritable to the terminal and add that rules into the grammar implicitly
                symb = fill.get(rule.right[1])
                # create rule replacing the original one
                created = type("ChomskyRight[" + rule.__name__ + "]",
                               (ChomskyTerminalReplaceRule,),
                               ChomskyTerminalReplaceRule.__dict__.copy())
                created.rule = ([rule.fromSymbol], [rule.right[0], symb])
                created.from_rule = rule
                created.replaced_index = 1
                # add it into the grammar
                grammar.rules.add(created)
                to_process.put(created)
    return grammar
