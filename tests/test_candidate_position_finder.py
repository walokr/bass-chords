from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.instruments.bass.bass import Bass
from bass_chords.theory.chord import Chord
from bass_chords.theory.note import Note
from bass_chords.instruments.bass.candidate_position_finder import CandidatePositionFinder


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
