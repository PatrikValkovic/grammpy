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

    def is_regular(self):
        return False

    def is_contextfree(self):
        return False

    def is_context(self):
        return False

    def is_unrestricted(self):
        return False
