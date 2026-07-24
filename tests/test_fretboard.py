from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.instruments.bass.position import Position
from bass_chords.theory.note import Note


def test_find_f():

    bass = Bass.standard()

    e = bass.strings[0]
    a = bass.strings[1]
    d = bass.strings[2]
    g = bass.strings[3]

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("F"))

    assert Position(d, 3) in positions
    assert Position(a, 8) in positions
    assert Position(e, 13) in positions
    assert Position(g, 10) in positions


def test_find_open_e():

    bass = Bass.standard()

    e = bass.strings[0]

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("E"))

    assert Position(e, 0) in positions


def test_find_positions_of_c():

    bass = Bass.standard()

    e = bass.strings[0]
    a = bass.strings[1]
    d = bass.strings[2]
    g = bass.strings[3]

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("C"))

    assert Position(a, 3) in positions
    assert Position(e, 8) in positions
    assert Position(d, 10) in positions
    assert Position(g, 17) in positions

    assert all(p.note == Note("C") for p in positions)


def test_find_returns_only_matching_notes():

    bass = Bass.standard()

    fretboard = Fretboard(bass)

    positions = fretboard.find(Note("C"))

    assert all(p.note == Note("C") for p in positions)


def test_note_at():

    bass = Bass.standard()

    e = bass.strings[0]
    a = bass.strings[1]
    g = bass.strings[3]

    fretboard = Fretboard(bass)

    assert fretboard.note_at(e, 0) == Note("E")
    assert fretboard.note_at(e, 1) == Note("F")
    assert fretboard.note_at(a, 3) == Note("C")
    assert fretboard.note_at(g, 12) == Note("G")
