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

        return (
            self._different_strings(combination)
            and self._inside_search_range(combination)
            and self._near_center_fret(combination)
        )

    def _near_center_fret(self, combination):

        # TODO:
        # Cuando SearchOptions.center_fret tenga un valor,
        # priorizar las combinaciones cercanas a esa zona.
        return True

    def _different_strings(self, combination):

        return (
            len({p.string for p in combination})
            == len(combination)
        )

    def find(self, chord: Chord):

        combinations = self.position_combinations(chord)

        return self.filter(combinations)

    def _inside_search_range(self, combination):

        return all(
            position.fret <= self.search_options.max_fret
            for position in combination
        )
