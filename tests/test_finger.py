from bass_chords.instruments.bass.finger import Finger


def test_finger_values():

    assert Finger.INDEX.value == 1
    assert Finger.MIDDLE.value == 2
    assert Finger.RING.value == 3
    assert Finger.PINKY.value == 4


def test_string_representation():

    assert str(Finger.INDEX) == "1"
    assert str(Finger.PINKY) == "4"
