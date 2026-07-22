from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note
from bass_chords.theory.pitch import Pitch


def test_create_bass():

    e = BassString(Pitch(Note("E"), 1))
    a = BassString(Pitch(Note("A"), 1))
    d = BassString(Pitch(Note("D"), 2))
    g = BassString(Pitch(Note("G"), 2))

    bass = Bass(
        strings=(e, a, d, g),
        frets=20,
    )

    assert bass.frets == 20
    assert bass.strings == (e, a, d, g)


def test_standard_bass():

    bass = Bass.standard()

    e = BassString(Pitch(Note("E"), 1))
    a = BassString(Pitch(Note("A"), 1))
    d = BassString(Pitch(Note("D"), 2))
    g = BassString(Pitch(Note("G"), 2))

    assert bass.frets == 20
    assert bass.strings == (e, a, d, g)