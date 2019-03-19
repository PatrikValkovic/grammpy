#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 08:54
:Licence MIT
Part of grammpy

"""

from .GrammpyException import GrammpyException

class CannotConvertException(GrammpyException, ValueError):
    """
    Library cant convert objects
    """
    pass