from bass_chords.theory.note import Note
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
