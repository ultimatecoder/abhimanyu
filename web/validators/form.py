#! /usr/bin/env python
from typing import Union

def is_blank(value: Union[str, None]) -> bool:
    """Checks that given value is blank or not"""
    if (not value) or (value.isspace()):
        return True
    else:
        return False
