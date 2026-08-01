from itertools import product

from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord
from bass_chords.search.search_options import SearchOptions

DEFAULT_MAX_SEARCH_FRET = 12


class CandidatePositionFinder:

    def __init__(
        self,
        fretboard: Fretboard,
        search_options: SearchOptions | None = None,
    ):
        self.fretboard = fretboard
        self.search_options = (
            search_options
            if search_options is not None
            else SearchOptions()
        )

    def positions_by_note(self, chord: Chord):

        return {
            note: self.fretboard.find(note)
            for note in chord.notes
        }

    def position_combinations(self, chord: Chord):

        positions = self.positions_by_note(chord)

        return tuple(
            product(*positions.values())
        )

    def filter(self, combinations):

        return tuple(
            combination
            for combination in combinations
            if self._is_candidate(combination)
        )

    def _is_candidate(self, combination):

        return all((
            self._different_strings(combination),
            self._inside_search_range(combination),
        ))

    def _different_strings(self, combination):

        return (
            len({p.string for p in combination})
            == len(combination)
        )

    def find(self, chord: Chord):

        combinations = self.position_combinations(chord)

        candidates = self.filter(combinations)

        return tuple(
            sorted(
                candidates,
                key=self._distance_to_center,
            )
        )

    def _inside_search_range(self, combination):

        return all(
            self.search_options.min_fret
            <= position.fret
            <= self.search_options.max_fret
            for position in combination
        )

    def _average_fret(self, combination):

        frets = tuple(
            position.fret
            for position in combination
        )

        return sum(frets) / len(frets)

    def _center_fret(self):

        return self.search_options.center_fret

    def _distance_to_center(self, combination):

        center = self._center_fret()

        if center is None:
            return 0

        return abs(
            self._average_fret(combination)
            - center
        )
