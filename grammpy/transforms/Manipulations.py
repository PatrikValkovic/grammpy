#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.12.2017 11:31
:Licence MIT
Part of grammpy

"""
import functools
import operator
from typing import TYPE_CHECKING, Callable, Union, Any, List

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
    def traverse(root, callback):
        # type: (Nonterminal, Callable[[Any, Callable], List]) -> List
        """
        Traverse AST based on callback.
        :param root: Root element of the parsed tree.
        :param callback: Function that accepts current node and callback c_2.
        Function must return nodes you want to traverse in the list.
        Its possible to call callback c_2 on any node to call the recursion.
        :return: Sequence of nodes to traverse.
        """

        def innerCallback(item):
            return callback(item, innerCallback)

        return callback(root, innerCallback)

    @staticmethod
    def traverseSeparated(root, callbackRules, callbackNonterminals, callbackTerminals):
        # type: (Nonterminal, Callable[[Rule, Callable], List], Callable[[Nonterminal, Callable], List], Callable[[Terminal, Callable], List]) -> List
        """
        Same as traverse method, but have different callbacks for rules, nonterminals and terminals.
        :param root: Root node of the parsed tree.
        :param callbackRules: Callback to call for every rule.
        :param callbackNonterminals: Callback to call for every nonterminal.
        :param callbackTerminals: Callback to call for every terminal.
        :return: Sequence of nodes to traverse.
        """

        def separateTraverse(item, callback):
            if isinstance(item, Rule):
                return callbackRules(item, callback)
            if isinstance(item, Nonterminal):
                return callbackNonterminals(item, callback)
            if isinstance(item, Terminal):
                return callbackTerminals(item, callback)

        return Traversing.traverse(root, separateTraverse)

    @staticmethod
    def preOrder(root):
        # type: (Nonterminal) -> List
        """
        Perform pre-order traversing. Expects tree like structure.
        :param root: Root tree of the parsed tree.
        :return: Sequence of nodes to traverse.
        """

        def travRule(item, callback):
            resp = [callback(ch) for ch in item.to_symbols]
            return functools.reduce(operator.add, resp, [item])

        def travNonterminals(item, callback):
            return [item] + callback(item.to_rule)

        def travTerms(item, callback):
            return [item]

        return Traversing.traverseSeparated(root, travRule, travNonterminals, travTerms)

    @staticmethod
    def postOrder(root):
        # type: (Nonterminal) -> List
        """
        Perform post-order traversing. Expects tree like structure.
        :param root: Root node of the parsed tree.
        :return: Sequence of nodes to traverse.
        """

        def travRule(item, callback):
            resp = [callback(ch) for ch in item.to_symbols]
            return functools.reduce(operator.add, resp, []) + [item]

        def travNonterminals(item, callback):
            return callback(item.to_rule) + [item]

        def travTerms(item, callback):
            return [item]

        return Traversing.traverseSeparated(root, travRule, travNonterminals, travTerms)

    @staticmethod
    def print(root, previous=0, defined=None, is_last=False):
        # type: (Union[Nonterminal,Terminal,Rule], int, List[int], bool)-> str
        """
        Transform the parsed tree to the string. You can see example output below.
        Expects tree like structure.

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
        :param previous: Number of columns defined before.
        :param defined: Number of lines defined before current column.
        :param is_last: If is current element the last child.
        :return: String representing the parsed tree.
        """
        defined = defined or []
        ret = ''
        # how far we are from the edge
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
        # print nonterminal and call recursion
        if isinstance(root, Nonterminal):
            ret += '(N)' + root.__class__.__name__ + '\n'
            ret += Traversing.print(root.to_rule, previous + 1, defined, True)
        # print terminal and end
        elif isinstance(root, Terminal):
            ret += '(T)' + str(root.s) + '\n'
            return ret
        # print rule and call recursion
        elif isinstance(root, Rule):
            # print the rule name
            ret += '(R)' + root.__class__.__name__ + '\n'
            # register new column
            defined.append(previous)
            # print all childs except the last one
            for i in range(len(root.to_symbols) - 1):
                ret += Traversing.print(root.to_symbols[i],
                                        previous + 1,
                                        defined,
                                        False)
            # unregister the column as last child print it automatically
            defined.pop()
            # print the last child
            ret += Traversing.print(root.to_symbols[-1],
                                    previous + 1,
                                    defined,
                                    True)
        return ret
