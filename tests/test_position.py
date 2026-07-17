from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.finger import Finger
from bass_chords.theory.note import Note


def test_create_position():

    pos = Position(
        string=BassString.A,
        fret=8,
        note=Note("F"),
        finger=Finger.RING,
    )

    assert pos.string == BassString.A
    assert pos.fret == 8
    assert pos.note == Note("F")
    assert pos.finger == Finger.RING
