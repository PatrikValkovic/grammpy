#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.12.2024 17:55
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING
from .create_first_table import create_first_table

if TYPE_CHECKING:  # pragma: no cover
    from .create_first_table import FirstTableType, FirstTableTypeValue
