from bass_chords.theory.interval import Interval
import pytest
from bass_chords.theory.note import Note


def test_create_interval():
    interval = Interval("1")

    assert interval.name == "1"


def test_minor_third():
    interval = Interval("b3")

    assert interval.semitones == 3


def test_perfect_fifth():
    interval = Interval("5")

    assert interval.semitones == 7


def test_invalid_interval():
    with pytest.raises(ValueError):
        Interval("pizza")


@pytest.mark.parametrize(
    "name,semitones",
    [
        ("1", 0),
        ("b2", 1),
        ("2", 2),
        ("#2", 3),
        ("b3", 3),
        ("3", 4),
        ("4", 5),
        ("#4", 6),
        ("b5", 6),
        ("5", 7),
        ("#5", 8),
        ("b6", 8),
        ("6", 9),
        ("#6", 10),
        ("b7", 10),
        ("7", 11),
    ],
)
def test_interval_semitones(name, semitones):
    assert Interval(name).semitones == semitones


def test_create_note_from_value():
    note = Note.from_value(3)

    assert note.name == "Eb"
    assert note.value == 3


def test_note_from_value_wraps_octave():
    note = Note.from_value(15)

    assert note.name == "Eb"
