#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .Constants import EPSILON


class Rule:
    right = [EPSILON]
    left = [EPSILON]
    rule = ([EPSILON], [EPSILON])
    rules = [([EPSILON], [EPSILON])]

    @staticmethod
    def is_regular():
        return False

    @staticmethod
    def is_contextfree():
        return False

    @staticmethod
    def is_context():
        return False

    @staticmethod
    def is_unrestricted():
        return False
