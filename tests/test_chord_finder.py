from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.chord_finder import ChordFinder
from bass_chords.instruments.bass.chord_shape import ChordShape
from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord


def test_create_chord_finder():

    fretboard = Fretboard(Bass.standard())

    finder = ChordFinder(fretboard)

    assert finder.fretboard is fretboard


def test_find_returns_tuple():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.find(
        Chord.parse("C")
    )

    assert isinstance(shapes, tuple)


def test_find_returns_chord_shapes():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.find(
        Chord.parse("C")
    )

    assert all(
        isinstance(shape, ChordShape)
        for shape in shapes
    )


def test_find_returns_empty_tuple_for_now():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.find(
        Chord.parse("C")
    )

    assert shapes == ()
