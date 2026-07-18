from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note


def test_find_f():

    fretboard = Fretboard()

    positions = fretboard.find(Note("F"))

    assert Position(BassString.D, 3) in positions
    assert Position(BassString.A, 8) in positions
    assert Position(BassString.E, 13) in positions


def test_find_open_e():

    fretboard = Fretboard()

    positions = fretboard.find(Note("E"))

    assert Position(BassString.E, 0) in positions


def test_find_returns_only_matching_notes():

    fretboard = Fretboard()

    positions = fretboard.find(Note("C"))

    assert all(p.note == Note("C") for p in positions)
