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


def test_create_bass2():

    bass = Bass(
        strings=(
            ...
        ),
        frets=20,
        scale_length=30,
    )

    assert bass.scale_length == 30


def test_standard_bass():

    bass = Bass.standard()

    assert bass.scale_length == 34


def test_standard_bass2():

    bass = Bass.standard()

    e = BassString(Pitch(Note("E"), 1))
    a = BassString(Pitch(Note("A"), 1))
    d = BassString(Pitch(Note("D"), 2))
    g = BassString(Pitch(Note("G"), 2))

    assert bass.frets == 20
    assert bass.strings == (e, a, d, g)


def test_create_short_scale_bass():

    bass = Bass(
        strings=(
            BassString.standard_e(),
            BassString.standard_a(),
            BassString.standard_d(),
            BassString.standard_g(),
        ),
        frets=20,
        scale_length=30,
    )

    assert bass.scale_length == 30


def test_fret_positions():

    bass = Bass.standard()

    assert bass.fret_position(0) == 0
    assert bass.fret_position(1) > 0
    assert bass.fret_position(2) > bass.fret_position(1)
    assert bass.fret_position(12) > bass.fret_position(11)


def test_fret_distance():

    bass = Bass.standard()

    assert bass.fret_distance(0, 0) == 0

    assert bass.fret_distance(0, 1) > 0

    assert (
        bass.fret_distance(1, 5)
        >
        bass.fret_distance(8, 12)
    )
