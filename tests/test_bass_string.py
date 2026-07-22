from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note
from bass_chords.theory.pitch import Pitch


def test_open_notes():

    e = BassString(Pitch(Note("E"), 1))
    a = BassString(Pitch(Note("A"), 1))
    d = BassString(Pitch(Note("D"), 2))
    g = BassString(Pitch(Note("G"), 2))

    assert e.note == Note("E")
    assert a.note == Note("A")
    assert d.note == Note("D")
    assert g.note == Note("G")


def test_note_at_fret():

    e = BassString(Pitch(Note("E"), 1))
    a = BassString(Pitch(Note("A"), 1))
    g = BassString(Pitch(Note("G"), 2))

    assert e.note_at(0) == Note("E")
    assert e.note_at(1) == Note("F")
    assert e.note_at(3) == Note("G")

    assert a.note_at(0) == Note("A")
    assert a.note_at(8) == Note("F")

    assert g.note_at(7) == Note("D")