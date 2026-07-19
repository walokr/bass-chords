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


def test_add11_formula():
    formula = ChordFormula("add11")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("11"),
    )


def test_add13_formula():
    formula = ChordFormula("add13")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("13"),
    )


def test_ninth_formula():
    formula = ChordFormula("9")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
    )


def test_major9_formula():
    formula = ChordFormula("maj9")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("7"),
        Interval("9"),
    )


def test_minor9_formula():
    formula = ChordFormula("m9")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
    )


def test_eleventh_formula():
    formula = ChordFormula("11")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
        Interval("11"),
    )


def test_thirteenth_formula():
    formula = ChordFormula("13")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
        Interval("11"),
        Interval("13"),
    )


def test_diminished_formula():
    formula = ChordFormula("dim")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("b5"),
    )


def test_augmented_formula():
    formula = ChordFormula("aug")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("#5"),
    )


def test_sus2_formula():
    formula = ChordFormula("sus2")

    assert formula.intervals == (
        Interval("1"),
        Interval("2"),
        Interval("5"),
    )


def test_sus4_formula():
    formula = ChordFormula("sus4")

    assert formula.intervals == (
        Interval("1"),
        Interval("4"),
        Interval("5"),
    )


def test_major6_formula():
    formula = ChordFormula("6")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("6"),
    )


def test_dominant7_flat5_formula():
    formula = ChordFormula("7b5")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("b5"),
        Interval("b7"),
    )


def test_dominant7_sharp5_formula():
    formula = ChordFormula("7#5")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("#5"),
        Interval("b7"),
    )


def test_dominant7_flat9_formula():
    formula = ChordFormula("7b9")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("b9"),
    )


def test_dominant7_sharp9_formula():
    formula = ChordFormula("7#9")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("#9"),
    )


def test_dominant7_sharp11_formula():
    formula = ChordFormula("7#11")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
        Interval("#11"),
    )


def test_dominant7_flat13_formula():
    formula = ChordFormula("7b13")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
        Interval("b13"),
    )


def test_minor6_formula():
    formula = ChordFormula("m6")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
        Interval("6"),
    )


def test_major11_formula():
    formula = ChordFormula("maj11")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("7"),
        Interval("9"),
        Interval("11"),
    )


def test_major13_formula():
    formula = ChordFormula("maj13")

    assert formula.intervals == (
        Interval("1"),
        Interval("3"),
        Interval("5"),
        Interval("7"),
        Interval("9"),
        Interval("11"),
        Interval("13"),
    )


def test_minor11_formula():
    formula = ChordFormula("m11")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
        Interval("11"),
    )


def test_minor13_formula():
    formula = ChordFormula("m13")

    assert formula.intervals == (
        Interval("1"),
        Interval("b3"),
        Interval("5"),
        Interval("b7"),
        Interval("9"),
        Interval("11"),
        Interval("13"),
    )


def test_invalid_formula():
    with pytest.raises(ValueError):
        ChordFormula("pizza")
