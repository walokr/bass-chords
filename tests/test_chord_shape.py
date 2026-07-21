from bass_chords.instruments.bass.chord_shape import ChordShape
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString


def test_create_chord_shape():

    shape = ChordShape(
        positions=(
            Position(BassString.E, 5),
            Position(BassString.A, 7),
            Position(BassString.D, 7),
            Position(BassString.G, 5),
        )
    )

    assert len(shape.positions) == 4

    assert shape.positions == (
        Position(BassString.E, 5),
        Position(BassString.A, 7),
        Position(BassString.D, 7),
        Position(BassString.G, 5),
    )