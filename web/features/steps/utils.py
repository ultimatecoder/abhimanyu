#! /usr/bin/env python

from typing import Union

value = Union[str, int, bool, float,]

def custom_assert(left: value, right: value) -> None:
    """Compares given values with built-in assert implementation.

    When things are compared with built-in assert method and if they are
    different in value then unhandled exception "AssertionError" do not guide
    which are the values both the elements. This method gives appropriate error
    message along with values of them.
    """
    error_message = f'"{left}" is not equal to "{right}"'
    assert left == right, error_message
