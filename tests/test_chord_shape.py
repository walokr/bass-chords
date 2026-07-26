from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.chord_shape import ChordShape
from bass_chords.instruments.bass.bass_string import BassString

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


def test_display_positions():

    e = BassString.standard_e()
    a = BassString.standard_a()
    d = BassString.standard_d()
    g = BassString.standard_g()

    shape = ChordShape(
        positions=(
            Position(e, 3),
            Position(a, 3),
            Position(d, 2),
            Position(g, 0),
        )
    )

    assert shape.display_positions == (
        Position(g, 0),
        Position(d, 2),
        Position(a, 3),
        Position(e, 3),
    )


def test_open_string_count():

    shape = ChordShape(
        positions=(
            Position(BassString.standard_e(), 0),
            Position(BassString.standard_a(), 3),
            Position(BassString.standard_d(), 0),
        )
    )

    assert shape.open_string_count == 2


def test_has_repeated_strings():

    e = BassString.standard_e()

    shape = ChordShape(
        positions=(
            Position(e, 3),
            Position(e, 8),
        )
    )

    assert shape.has_repeated_strings


def test_has_not_repeated_strings():

    shape = ChordShape(
        positions=(
            Position(BassString.standard_e(), 3),
            Position(BassString.standard_a(), 3),
        )
    )

    assert not shape.has_repeated_strings


def test_is_playable():

    shape = ChordShape(
        positions=(
            Position(BassString.standard_e(), 3),
            Position(BassString.standard_a(), 3),
            Position(BassString.standard_d(), 2),
        )
    )

    assert shape.is_playable


def test_is_not_playable_with_repeated_strings():

    e = BassString.standard_e()

    shape = ChordShape(
        positions=(
            Position(e, 3),
            Position(e, 8),
        )
    )

    assert not shape.is_playable


def test_is_not_playable_with_large_span():

    shape = ChordShape(
        positions=(
            Position(BassString.standard_e(), 1),
            Position(BassString.standard_a(), 7),
        )
    )

    assert not shape.is_playable
