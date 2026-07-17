import pytest

from bass_chords.theory.chord import Chord
from bass_chords.theory.note import Note


def test_parse_f7():
    chord = Chord.parse("F7")

    assert chord.root == Note("F")
    assert chord.symbol == "7"


def test_parse_bbmaj7():
    chord = Chord.parse("Bbmaj7")

    assert chord.root == Note("Bb")
    assert chord.symbol == "maj7"


def test_parse_c_sharp_minor7():
    chord = Chord.parse("C#m7")

    assert chord.root == Note("C#")
    assert chord.symbol == "m7"


def test_parse_major():
    chord = Chord.parse("C")

    assert chord.root == Note("C")
    assert chord.symbol == ""


def test_invalid_root():
    with pytest.raises(ValueError):
        Chord.parse("H7")
