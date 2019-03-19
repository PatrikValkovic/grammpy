#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 09.03.2019 17:31
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import Type, TYPE_CHECKING

from ... import Nonterminal

if TYPE_CHECKING:  # pragma: no cover
    from ... import Rule


def _is_unit(rule):
    # type: (Type[Rule]) -> bool
    """
    Check if parameter is unit rule.
    :param rule: Object to check.
    :return: True if is parameter unit rule, false otherwise.
    """
    return len(rule.left) == 1 and len(rule.right) == 1 and \
           isclass(rule.fromSymbol) and isclass(rule.toSymbol) and \
           issubclass(rule.fromSymbol, Nonterminal) and issubclass(rule.toSymbol, Nonterminal)
