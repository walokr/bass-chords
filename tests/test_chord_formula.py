import pytest

from bass_chords.theory.chord_formula import ChordFormula
from bass_chords.theory.interval import Interval


def test_major_formula():
    formula = ChordFormula("")

    assert formula.symbol == ""
    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
    )


def test_minor_formula():
    formula = ChordFormula("m")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
    )


def test_dominant7_formula():
    formula = ChordFormula("7")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
    )


def test_invalid_formula():
    with pytest.raises(ValueError):
        ChordFormula("pizza")
