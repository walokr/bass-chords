from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.instruments.bass.bass import Bass
from bass_chords.theory.chord import Chord
from bass_chords.theory.note import Note
from bass_chords.instruments.bass.candidate_position_finder import CandidatePositionFinder
from bass_chords.search.search_options import SearchOptions
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.bass_string import BassString


def test_positions_by_note():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard())
    )

    positions = finder.positions_by_note(
        Chord.parse("C")
    )

    assert positions.keys() == {
        Note("C"),
        Note("E"),
        Note("G"),
    }

    assert len(positions[Note("C")]) > 0
    assert len(positions[Note("E")]) > 0
    assert len(positions[Note("G")]) > 0


def test_position_combinations():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard())
    )

    combinations = finder.position_combinations(
        Chord.parse("C")
    )

    assert isinstance(combinations, tuple)

    assert len(combinations) > 0

    assert all(
        len(combination) == 3
        for combination in combinations
    )


def test_find():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard())
    )

    candidates = finder.find(
        Chord.parse("C")
    )

    assert isinstance(candidates, tuple)

    assert len(candidates) > 0

    assert all(
        len({p.string for p in combination})
        == len(combination)
        for combination in candidates
    )


def test_max_fret_limits_candidates():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard()),
        SearchOptions(max_fret=5),
    )

    candidates = finder.find(
        Chord.parse("C")
    )

    assert all(
        all(
            position.fret <= 5
            for position in combination
        )
        for combination in candidates
    )


def test_respects_min_fret():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard()),
        SearchOptions(min_fret=5),
    )

    combination = (
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_a(), 5),
        Position(BassString.standard_d(), 5),
    )

    assert not finder._inside_search_range(combination)


def test_accepts_positions_above_min_fret():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard()),
        SearchOptions(min_fret=5),
    )

    combination = (
        Position(BassString.standard_e(), 5),
        Position(BassString.standard_a(), 7),
        Position(BassString.standard_d(), 8),
    )

    assert finder._inside_search_range(combination)


def test_center_fret():

    finder = CandidatePositionFinder(
        Fretboard(Bass.standard()),
        SearchOptions(center_fret=7),
    )

    assert finder._center_fret() == 7
