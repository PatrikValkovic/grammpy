#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 08:46
:Licence MIT
Part of grammpy

"""

from .CannotConvertException import CannotConvertException


class NotASingleSymbolException(CannotConvertException):
    """
    More symbols defined at the place where one symbol is expected
    """
    def __init__(self, symbols):
        self.symbols = symbols
