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


def test_major7_formula():
    formula = ChordFormula("maj7")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("7"),
    )


def test_minor7_formula():
    formula = ChordFormula("m7")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
        Interval("b7"),
    )


def test_minor_major7_formula():
    formula = ChordFormula("mMaj7")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
        Interval("7"),
    )


def test_diminished7_formula():
    formula = ChordFormula("dim7")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("b5"),
        Interval("bb7"),
    )

def test_add2_formula():
    formula = ChordFormula("add2")

    assert formula.intervals == (
        Interval("1"),
        Interval("2"),
        Interval("3"),
        Interval("5"),
    )

def test_add4_formula():
    formula = ChordFormula("add4")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("4"),
        Interval("5"),
    )

def test_add9_formula():
    formula = ChordFormula("add9")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("9"),
    )


def test_half_diminished_formula():
    formula = ChordFormula("m7b5")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("b5"),
        Interval("b7"),
    )


def test_invalid_formula():
    with pytest.raises(ValueError):
        ChordFormula("pizza")
