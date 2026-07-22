from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.finger import Finger
from bass_chords.theory.note import Note
from bass_chords.instruments.bass.bass import Bass

bass = Bass.standard()

e = bass.strings[0]
a = bass.strings[1]
d = bass.strings[2]
g = bass.strings[3]


def test_position_calculates_note():

    pos = Position(
        string=a,
        fret=8,
    )

    assert pos.note == Note("F")


def test_open_string():

    pos = Position(
        string=e,
        fret=0,
    )

    assert pos.note == Note("E")


def test_is_open():

    pos = Position(
        string=g,
        fret=0,
    )

    assert pos.is_open


def test_is_not_open():

    pos = Position(
        string=g,
        fret=5,
    )

    assert not pos.is_open


def test_with_finger():

    pos = Position(
        string=d,
        fret=7,
        finger=Finger.MIDDLE,
    )

    assert pos.finger == Finger.MIDDLE


def test_string_representation():

    pos = Position(
        string=a,
        fret=8,
        finger=Finger.RING,
    )

    assert str(pos) == "A8 F (3)"
