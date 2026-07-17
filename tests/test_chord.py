from bass_chords.theory.chord import Chord
from bass_chords.theory.note import Note


def test_f7_notes():
    chord = Chord(Note("F"), "7")

    assert chord.root == Note("F")
    assert chord.symbol == "7"

    assert chord.notes == (
        Note("F"),
        Note("A"),
        Note("C"),
        Note("Eb"),
    )
