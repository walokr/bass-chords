from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.chord_shape import ChordShape


bass = Bass.standard()

e = bass.strings[0]
a = bass.strings[1]
d = bass.strings[2]
g = bass.strings[3]


def test_create_chord_shape():

    shape = ChordShape(
        positions=(
            Position(e, 5),
            Position(a, 7),
            Position(d, 7),
            Position(g, 5),
        )
    )

    assert len(shape.positions) == 4


def test_lowest_fret():

    shape = ChordShape(
        positions=(
            Position(e, 5),
            Position(a, 7),
            Position(d, 2),
            Position(g, 9),
        )
    )

    assert shape.lowest_fret == 2


def test_highest_fret():

    shape = ChordShape(
        positions=(
            Position(e, 5),
            Position(a, 7),
            Position(d, 2),
            Position(g, 9),
        )
    )

    assert shape.highest_fret == 9


def test_span():

    shape = ChordShape(
        positions=(
            Position(e, 5),
            Position(a, 7),
            Position(d, 2),
            Position(g, 9),
        )
    )

    assert shape.span == 7


def test_open_strings():

    shape = ChordShape(
        positions=(
            Position(e, 0),
            Position(a, 2),
            Position(d, 2),
            Position(g, 0),
        )
    )

    assert shape.open_strings == (
        Position(e, 0),
        Position(g, 0),
    )


def test_fretted_positions():

    shape = ChordShape(
        positions=(
            Position(e, 0),
            Position(a, 2),
            Position(d, 2),
            Position(g, 0),
        )
    )

    assert shape.fretted_positions == (
        Position(a, 2),
        Position(d, 2),
    )


def test_lowest_fretted_fret():

    shape = ChordShape(
        positions=(
            Position(e, 0),
            Position(a, 2),
            Position(d, 5),
            Position(g, 7),
        )
    )

    assert shape.lowest_fretted_fret == 2


def test_lowest_fretted_fret_all_open():

    shape = ChordShape(
        positions=(
            Position(e, 0),
            Position(a, 0),
            Position(d, 0),
            Position(g, 0),
        )
    )

    assert shape.lowest_fretted_fret is None
