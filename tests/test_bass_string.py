from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note


def test_open_notes():

    assert BassString.E.open_note == Note("E")
    assert BassString.A.open_note == Note("A")
    assert BassString.D.open_note == Note("D")
    assert BassString.G.open_note == Note("G")


def test_note_at_fret():

    assert BassString.E.note_at(0) == Note("E")
    assert BassString.E.note_at(1) == Note("F")
    assert BassString.E.note_at(3) == Note("G")

    assert BassString.A.note_at(0) == Note("A")
    assert BassString.A.note_at(8) == Note("F")

    assert BassString.G.note_at(7) == Note("D")
