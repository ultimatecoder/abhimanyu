#! /usr/bin/env python

import pytest

from .. import utils


def _get_error_message(left: utils.value, right: utils.value) -> str:
    return f'"{left} is not equal to "{right}"'


def test_custom_assertwith_equal_values():
    sample_values = (
        ("A", "A"),
        ("", ""),
        (False, False),
        (" ", " "),
    )
    for left, right in sample_values:
        utils.custom_assert(left, right)

def test_custom_assert_with_unequal_values():
    sample_values = (
        ("A", "B"),
        (2, 5),
        ("test", "test1"),
        ("", "test"),
        ("  ", " ")
    )
    for left, right in sample_values:
        with pytest.raises(AssertionError) as assertion_error:
            utils.custom_assert(left, right)
            assert  _get_error_message(left, right) == str(
                assertion_error.value
            )
