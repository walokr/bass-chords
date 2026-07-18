from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.finger import Finger
from bass_chords.theory.note import Note


def test_position_calculates_note():

    pos = Position(
        string=BassString.A,
        fret=8,
    )

    assert pos.note == Note("F")


def test_open_string():

    pos = Position(
        string=BassString.E,
        fret=0,
    )

    assert pos.note == Note("E")


def test_is_open():

    pos = Position(
        string=BassString.G,
        fret=0,
    )

    assert pos.is_open


def test_is_not_open():

    pos = Position(
        string=BassString.G,
        fret=5,
    )

    assert not pos.is_open


def test_with_finger():

    pos = Position(
        string=BassString.D,
        fret=7,
        finger=Finger.MIDDLE,
    )

    assert pos.finger == Finger.MIDDLE


def test_string_representation():

    pos = Position(
        string=BassString.A,
        fret=8,
        finger=Finger.RING,
    )

    assert str(pos) == "A8 F (3)"
