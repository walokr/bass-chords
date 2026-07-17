from bass_chords.instruments.bass.tuning import BassTuning
from bass_chords.theory.note import Note


def test_standard_tuning():

    tuning = BassTuning.standard()

    assert tuning.strings == (
        Note("E"),
        Note("A"),
        Note("D"),
        Note("G"),
    )
