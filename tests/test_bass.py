from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.bass_string import BassString


def test_create_bass():
    bass = Bass(
        strings=(
            BassString.E,
            BassString.A,
            BassString.D,
            BassString.G,
        ),
        frets=20,
    )

    assert bass.frets == 20
    assert bass.strings == (
        BassString.E,
        BassString.A,
        BassString.D,
        BassString.G,
    )


def test_standard_bass():
    bass = Bass.standard()

    assert bass.frets == 20
    assert bass.strings == (
        BassString.E,
        BassString.A,
        BassString.D,
        BassString.G,
    )
