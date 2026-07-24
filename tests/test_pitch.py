from bass_chords.theory.note import Note
from bass_chords.theory.pitch import Pitch


def test_create_pitch():

    pitch = Pitch(Note("E"), 1)

    assert pitch.note == Note("E")
    assert pitch.octave == 1


def test_pitch_value():

    assert Pitch(Note("C"), 1).value == 12
    assert Pitch(Note("E"), 1).value == 16
    assert Pitch(Note("A"), 1).value == 21
    assert Pitch(Note("G"), 2).value == 31


def test_pitch_equality():

    assert Pitch(Note("E"), 1) == Pitch(Note("E"), 1)


def test_pitch_string():

    assert str(Pitch(Note("E"), 1)) == "E1"
