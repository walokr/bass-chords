from bass_chords.search.search_options import SearchOptions
from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.instruments.bass.candidate_position_finder import CandidatePositionFinder
from bass_chords.instruments.bass.bass import Bass
from bass_chords.search.search_options import DEFAULT_MAX_SEARCH_FRET


def test_default_values():

    options = SearchOptions()

    assert options.max_fret == DEFAULT_MAX_SEARCH_FRET
    assert options.center_fret is None
    assert options.movement_preference == "any"


def test_default_search_options():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard())
    )

    assert finder.search_options == SearchOptions()


def test_custom_search_options():

    options = SearchOptions(max_fret=7)

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard()),
        options,
    )

    assert finder.search_options is options
