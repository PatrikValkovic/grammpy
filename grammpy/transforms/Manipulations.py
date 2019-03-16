#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.12.2017 11:31
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING, Callable, Union, Any, Generator
from .. import Nonterminal, Terminal, Rule

if TYPE_CHECKING:  # pragma: no cover
    from ..representation.support._RuleConnectable import _RuleConnectable


class Manipulations:
    """
    Class that aggregate functions modifying the parsed tree.
    """

    @staticmethod
    def replaceRule(oldRule, newRule):
        # type: (Rule, Rule) -> Rule
        """
        Replace instance of Rule with another one.
        :param oldRule: Instance in the tree.
        :param newRule: Instance to replace with.
        :return: New instance attached to the tree.
        """
        for par in oldRule.from_symbols:
            par._set_to_rule(newRule)
            newRule._from_symbols.append(par)
        for ch in oldRule.to_symbols:
            ch._set_from_rule(newRule)
            newRule._to_symbols.append(ch)
        return newRule

    @staticmethod
    def replaceNode(oldNode, newNode):
        # type: (_RuleConnectable, _RuleConnectable) -> _RuleConnectable
        """
        Replace instance of Nonterminal or Terminal in the tree with another one.
        :param oldNode: Old nonterminal or terminal already in the tree.
        :param newNode: Instance of nonterminal or terminal to replace with.
        :return: Instance `newNode` in the tree.
        """
        if oldNode.from_rule is not None and len(oldNode.from_rule.to_symbols) > 0:
            indexParent = oldNode.from_rule.to_symbols.index(oldNode)
            oldNode.from_rule.to_symbols[indexParent] = newNode
            newNode._set_from_rule(oldNode.from_rule)
        if oldNode.to_rule is not None and len(oldNode.to_rule.from_symbols) > 0:
            indexChild = oldNode.to_rule.from_symbols.index(oldNode)
            oldNode.to_rule._from_symbols[indexChild] = newNode
            newNode._set_to_rule(oldNode.to_rule)
        return newNode

    @staticmethod
    def replace(oldEl, newEl):
        # type: (Union[Rule, _RuleConnectable], Union[Rule, _RuleConnectable]) -> Union[Rule, _RuleConnectable]
        """
        Replace element in the parsed tree. Can be nonterminal, terminal or rule.
        :param oldEl: Element already in the tree.
        :param newEl: Element to replace with.
        :return: New element attached to the tree.
        """
        if isinstance(oldEl, Rule):
            return Manipulations.replaceRule(oldEl, newEl)
        if isinstance(oldEl, (Nonterminal, Terminal)):
            return Manipulations.replaceNode(oldEl, newEl)


class Traversing:
    """
    Class that aggregates functions to traverse the parsed tree.
    """

    @staticmethod
    def traverse(root, callback, *args, **kwargs):
        # type: (Nonterminal, Callable[[Any, Callable, Any, Any], Generator], Any, Any) -> Generator
        """
        Traverse AST based on callback.
        :param root: Root element of the parsed tree.
        :param callback: Function that accepts current node, callback `c_2` and parameters from the parent.
        Function must yield individual values.
        Its possible to yield callback c_2 **call** on any node to call the recursion.
        The callback can accept parameters from the parent call.
        The root will receive parameters from the `traverse` call.

        Example of pre-order traversing:
        def traverse_func(item, callback):
            if isinstance(item, Rule):
                yield item
                for el in item.to_symbols:
                    yield callback(el)
            elif isinstance(item, Nonterminal):
                yield item
                yield callback(item.to_rule)
            else:
                yield item

        :return: Sequence of nodes to traverse.
        """
        class MyGenerator:
            def __init__(self, gen):
                self._gen = gen
            def __next__(self):
                return next(self._gen)

        def innerCallback(item, *args, **kwargs):
            return MyGenerator(callback(item, innerCallback, *args, **kwargs))

        to_call = list()
        to_call.append(innerCallback(root, *args, **kwargs))
        while len(to_call) > 0:
            current = to_call.pop()
            try:
                el = next(current)
                to_call.append(current)
                if isinstance(el, MyGenerator):
                    to_call.append(el)
                else:
                    yield el
            except StopIteration:
                continue

    @staticmethod
    def traverseSeparated(root, callbackRules, callbackNonterminals, callbackTerminals, *args, **kwargs):
        # type: (Nonterminal, Callable[[Rule, Callable, Any, Any], Generator], Callable[[Nonterminal, Callable, Any, Any], Generator], Callable[[Terminal, Callable, Any, Any], Generator], Any, Any) -> Generator
        """
        Same as traverse method, but have different callbacks for rules, nonterminals and terminals.
        Functions accepts current node, callback `c_2` and parameters from the parent.
        Functions must yield individual values.
        Its possible to yield callback c_2 **call** on any node to call the recursion.
        The callback can accept parameters from the parent call.
        The root will receive parameters from the `traverseSeparated` call.
        :param root: Root node of the parsed tree.
        :param callbackRules: Function to call for every rule.
        :param callbackNonterminals: Function to call for every nonterminal.
        :param callbackTerminals: Function to call for every terminal.
        :return: Sequence of nodes to traverse.
        """

        def separateTraverse(item, callback, *args, **kwargs):
            if isinstance(item, Rule):
                return callbackRules(item, callback, *args, **kwargs)
            if isinstance(item, Nonterminal):
                return callbackNonterminals(item, callback, *args, **kwargs)
            if isinstance(item, Terminal):
                return callbackTerminals(item, callback, *args, **kwargs)

        return Traversing.traverse(root, separateTraverse, *args, **kwargs)

    @staticmethod
    def preOrder(root):
        # type: (Nonterminal) -> Generator
        """
        Perform pre-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root tree of the parsed tree.
        :return: Sequence of nodes to traverse.
        """

        def travRule(item, callback):
            yield item
            for el in item.to_symbols:
                yield callback(el)

        def travNonterminals(item, callback):
            yield item
            yield callback(item.to_rule)

        def travTerms(item, callback):
            yield item

        return Traversing.traverseSeparated(root, travRule, travNonterminals, travTerms)

    @staticmethod
    def postOrder(root):
        # type: (Nonterminal) -> Generator
        """
        Perform post-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root node of the parsed tree.
        :return: Sequence of nodes to traverse.
        """

        def travRule(item, callback):
            for el in item.to_symbols:
                yield callback(el)
            yield item

        def travNonterminals(item, callback):
            yield callback(item.to_rule)
            yield item

        def travTerms(item, callback):
            yield item

        return Traversing.traverseSeparated(root, travRule, travNonterminals, travTerms)

    @staticmethod
    def print(root):
        # type: (Union[Nonterminal,Terminal,Rule])-> str
        """
        Transform the parsed tree to the string. Expects tree like structure.
        You can see example output below.

        (R)SplitRules26
        |--(N)Iterate
        |  `--(R)SplitRules30
        |     `--(N)Symb
        |        `--(R)SplitRules4
        |           `--(T)e
        `--(N)Concat
           `--(R)SplitRules27
              `--(N)Iterate
                 `--(R)SplitRules30
                    `--(N)Symb
                       `--(R)SplitRules5
                          `--(T)f

        :param root: Root node of the parsed tree.
        :return: String representing the parsed tree (ends with newline).
        """
        # print the part before the element
        def print_before(previous=0, defined=None, is_last=False):
            defined = defined or {}
            ret = ''
            if previous != 0:
                for i in range(previous - 1):
                    # if the column is still active write |
                    if i in defined:
                        ret += '|  '
                    # otherwise just print space
                    else:
                        ret += '   '
                # if is current element last child, don't print |-- but `-- instead
                ret += '`--' if is_last else '|--'
            return ret

        # print the terminal
        def terminal_traverse(term, callback, previous=0, defined=None, is_last=False):
            before = print_before(previous, defined, is_last)
            yield before + '(T)' + str(term.s) + '\n'

        # print the nonterminal
        def nonterminal_traverse(nonterm, callback, previous=0, defined=None, is_last=False):
            before = print_before(previous, defined, is_last)
            yield before + '(N)' + nonterm.__class__.__name__ + '\n'
            yield callback(nonterm.to_rule, previous + 1, defined, True)

        # print the rule
        def rule_traverse(rule, callback, previous=0, defined=None, is_last=False):
            # print the rule name
            before = print_before(previous, defined, is_last)
            yield before + '(R)' + rule.__class__.__name__ + '\n'
            # register new column
            defined = defined or set()
            defined.add(previous)
            # print all childs except the last one
            for i in range(len(rule.to_symbols) - 1):
                yield callback(rule.to_symbols[i], previous + 1, defined, False)
            # unregister the column as last child print it automatically
            defined.remove(previous)
            yield callback(rule.to_symbols[-1], previous + 1, defined, True)

        res = Traversing.traverseSeparated(root,
                                           rule_traverse,
                                           nonterminal_traverse,
                                           terminal_traverse)
        return str.join("", res)
