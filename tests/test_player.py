from bass_chords.instruments.bass.bass import Bass
from bass_chords.player.player import Player


def test_create_player():

    player = Player()

    assert player.max_reach_mm == 90.0


def test_create_player_with_custom_reach():

    player = Player(max_reach_mm=105.5)

    assert player.max_reach_mm == 105.5


def test_short_scale_requires_less_reach():

    long_bass = Bass.standard()

    short_bass = Bass(
        strings=long_bass.strings,
        frets=20,
        scale_length=30,
    )

    assert (
        short_bass.fret_distance_mm(1, 4)
        <
        long_bass.fret_distance_mm(1, 4)
    )


def test_player_reach_is_not_enough_for_large_stretch():

    bass = Bass.standard()
    player = Player(max_reach_mm=40)

    assert (
        bass.fret_distance_mm(1, 5)
        > player.max_reach_mm
    )
