#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.01.2019 23:30
:Licence GNUv3
Part of grammpy

"""
from typing import Type, TYPE_CHECKING, List, Tuple
from . import Rule as _Rule

if TYPE_CHECKING:
    from .. import Rule


class SplitRule(_Rule):

    @staticmethod
    def _create_class(rule, index):
        # type: (Type[Rule], int) -> Type[SplitRule]
        """
        Create subtype of SplitRule based on rule
        :param rule: Rule to be used for new class
        :return: Class inherited from SplitRule
        """
        name = 'SplitRule_(' + str(rule.__name__) + ')_' + str(index)
        created = type(name, (SplitRule,), SplitRule.__dict__.copy())  # type: Type[SplitRule]
        created.rule = rule.rules[index]
        created.rule_index = index
        created.from_rule = rule
        return created

    from_rule = None  # type: Type[Rule]
    rule_index = None  # type: int
    rule = None  # type: Tuple[List[object], List[object]]
