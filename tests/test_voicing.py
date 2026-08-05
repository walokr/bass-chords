from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.voicing import Voicing
from bass_chords.theory.note import Note
from bass_chords.theory.pitch import Pitch


def test_positions():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_a(), 2),
    ))

    assert len(voicing.positions) == 2


def test_notes():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_a(), 2),
    ))

    assert voicing.notes == (
        Note("G"),
        Note("B"),
    )


def test_average_fret():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 5),
    ))

    assert voicing.average_fret == 10 / 3


def test_lowest_fret():

    voicing = Voicing((
        Position(BassString.standard_e(), 5),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 7),
    ))

    assert voicing.lowest_fret == 2


def test_highest_fret():

    voicing = Voicing((
        Position(BassString.standard_e(), 5),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 7),
    ))

    assert voicing.highest_fret == 7


def test_span():

    voicing = Voicing((
        Position(BassString.standard_e(), 5),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 7),
    ))

    assert voicing.span == 5


def test_has_not_repeated_strings():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 5),
    ))

    assert voicing.has_repeated_strings is False


def test_has_repeated_strings():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_e(), 5),
    ))

    assert voicing.has_repeated_strings is True


def test_fret_range():

    voicing = Voicing((
        Position(BassString.standard_e(), 5),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 7),
    ))

    assert voicing.fret_range == (2, 7)


def test_lowest_pitch():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),   # G1
        Position(BassString.standard_a(), 2),   # B1
        Position(BassString.standard_d(), 5),   # G2
    ))

    assert voicing.lowest_pitch == Pitch(Note("G"), 1)


def test_highest_pitch():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),   # G1
        Position(BassString.standard_a(), 2),   # B1
        Position(BassString.standard_d(), 5),   # G2
    ))

    assert voicing.highest_pitch == Pitch(Note("G"), 2)
