#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 08:46
:Licence GNUv3
Part of grammpy

"""

from .CannotConvertException import CannotConvertException


class NotASingleSymbolException(CannotConvertException):
    def __init__(self, symbols):
        self.symbols = symbols
