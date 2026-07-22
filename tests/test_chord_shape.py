from bass_chords.instruments.bass.chord_shape import ChordShape
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.bass import Bass

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

    assert shape.positions == (
        Position(e, 5),
        Position(a, 7),
        Position(d, 7),
        Position(g, 5),
    )