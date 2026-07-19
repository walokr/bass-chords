from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note


def test_find_f():

    bass = Bass.standard()

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("F"))

    assert Position(BassString.D, 3) in positions
    assert Position(BassString.A, 8) in positions
    assert Position(BassString.E, 13) in positions


def test_find_open_e():

    bass = Bass.standard()

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("E"))

    assert Position(BassString.E, 0) in positions


def test_find_positions_of_c():

    bass = Bass.standard()

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("C"))

    assert Position(BassString.A, 3) in positions
    assert Position(BassString.E, 8) in positions
    assert Position(BassString.D, 10) in positions
    assert Position(BassString.G, 17) in positions

    assert all(p.note == Note("C") for p in positions)


def test_find_returns_only_matching_notes():

    bass = Bass.standard()

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("C"))

    assert all(p.note == Note("C") for p in positions)


def test_note_at():

    fretboard = Fretboard(Bass.standard())

    assert fretboard.note_at(BassString.E, 0) == Note("E")
    assert fretboard.note_at(BassString.E, 1) == Note("F")
    assert fretboard.note_at(BassString.A, 3) == Note("C")
    assert fretboard.note_at(BassString.G, 12) == Note("G")
