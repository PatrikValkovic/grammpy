#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 08.07.2017 14:03
:Licence GNUv3
Part of grammpy

"""
from typing import Any


class GrammpyException(Exception):
    """
    Base class for all exceptions
    """
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)