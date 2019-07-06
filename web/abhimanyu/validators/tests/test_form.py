#! /usr/bin/env python

from .. import form


def test_is_blank():
    sample_inputs_and_expected_answers = (
        ("", True),
        (None, True),
        ("hello world", False),
        ("1234", False),
        ("hello world", False),
        ("  ", True),
        ("%%%$$", False)
    )
    for sample_input, expected_answer in sample_inputs_and_expected_answers:
        assert form.is_blank(sample_input) == expected_answer
