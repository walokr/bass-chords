from bass_chords.theory.note import Note
from bass_chords.theory.interval import Interval
import pytest


def test_create_note():
    note = Note("C")

    assert note.name == "C"


def test_note_is_case_insensitive():
    note = Note("c")

    assert note.name == "C"


def test_invalid_note():
    with pytest.raises(ValueError):
        Note("H")


def test_note_is_case_insensitive_flat():
    note = Note("eb")
    assert note.name == "Eb"
    

def test_note_is_case_insensitive_sharp():
    note = Note("f#")
    assert note.name == "F#"


def test_transpose_minor_third():
    assert Note("C").transpose(Interval("b3")) == Note("Eb")


def test_transpose_perfect_fifth():
    assert Note("F").transpose(Interval("5")) == Note("C")


def test_transpose_major_third():
    assert Note("G").transpose(Interval("3")) == Note("B")


def test_transpose_wrap_octave():
    assert Note("B").transpose(Interval("b2")) == Note("C")


def test_note_from_value():
    note = Note.from_value(3)
    assert note == Note("Eb")
    

def test_note_from_value_prefer_sharp():
    note = Note.from_value(
        3,
        Accidental.SHARP,
    )
    assert note == Note("D#")


def test_note_from_value_prefer_flat():
    note = Note.from_value(
        10,
        Accidental.FLAT,
    )
    assert note == Note("Bb")
    
from bass_chords.theory.interval import Interval
from bass_chords.theory.note import Note


def test_transpose_minor_third():
    assert Note("C").transpose(
        Interval("b3")
    ) == Note("Eb")
    

def test_transpose_perfect_fifth():
    assert Note("F").transpose(
        Interval("5")
    ) == Note("C")
    
def test_transpose_wrap_octave():
    assert Note("B").transpose(
        Interval("b2")
    ) == Note("C")


from bass_chords.theory.accidental import Accidental


def test_transpose_prefer_sharp():
    assert (
        Note("C").transpose(
            Interval("b3"),
            Accidental.SHARP,
        )
        == Note("D#")
    )


