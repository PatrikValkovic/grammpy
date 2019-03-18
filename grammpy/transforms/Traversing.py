#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 18.03.2019 18:17
:Licence MIT
Part of grammpy

"""
from typing import Callable, Any, Union, Generator
from grammpy import Rule, Nonterminal, Terminal


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

        def inner_callback(item, *args, **kwargs):
            return MyGenerator(callback(item, inner_callback, *args, **kwargs))

        to_call = list()
        to_call.append(inner_callback(root, *args, **kwargs))
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
    def traverse_separated(root, callbackRules, callbackNonterminals, callbackTerminals, *args, **kwargs):
        # type: (Nonterminal, Callable[[Rule, Callable, Any, Any], Generator], Callable[[Nonterminal, Callable, Any, Any], Generator], Callable[[Terminal, Callable, Any, Any], Generator], Any, Any) -> Generator
        """
        Same as traverse method, but have different callbacks for rules, nonterminals and terminals.
        Functions accepts current node, callback `c_2` and parameters from the parent.
        Functions must yield individual values.
        Its possible to yield callback c_2 **call** on any node to call the recursion.
        The callback can accept parameters from the parent call.
        The root will receive parameters from the `traverse_separated` call.
        :param root: Root node of the parsed tree.
        :param callbackRules: Function to call for every rule.
        :param callbackNonterminals: Function to call for every nonterminal.
        :param callbackTerminals: Function to call for every terminal.
        :return: Sequence of nodes to traverse.
        """

        def separate_traverse_callback(item, callback, *args, **kwargs):
            if isinstance(item, Rule):
                return callbackRules(item, callback, *args, **kwargs)
            if isinstance(item, Nonterminal):
                return callbackNonterminals(item, callback, *args, **kwargs)
            if isinstance(item, Terminal):
                return callbackTerminals(item, callback, *args, **kwargs)

        return Traversing.traverse(root, separate_traverse_callback, *args, **kwargs)

    @staticmethod
    def pre_order(root):
        # type: (Nonterminal) -> Generator
        """
        Perform pre-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root tree of the parsed tree.
        :return: Sequence of nodes to traverse.
        """

        def traverse_rule(item, callback):
            yield item
            for el in item.to_symbols:
                yield callback(el)

        def traverse_nonterminal(item, callback):
            yield item
            yield callback(item.to_rule)

        def traverse_terminal(item, callback):
            yield item

        return Traversing.traverse_separated(root, traverse_rule, traverse_nonterminal, traverse_terminal)

    @staticmethod
    def post_order(root):
        # type: (Nonterminal) -> Generator
        """
        Perform post-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root node of the parsed tree.
        :return: Sequence of nodes to traverse.
        """

        def traverse_rule(item, callback):
            for el in item.to_symbols:
                yield callback(el)
            yield item

        def traverse_nonterminal(item, callback):
            yield callback(item.to_rule)
            yield item

        def traverse_terminal(item, callback):
            yield item

        return Traversing.traverse_separated(root, traverse_rule, traverse_nonterminal, traverse_terminal)

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

        res = Traversing.traverse_separated(root, rule_traverse, nonterminal_traverse, terminal_traverse)
        return str.join("", res)
