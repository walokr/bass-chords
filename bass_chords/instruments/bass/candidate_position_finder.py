from itertools import product

from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord

DEFAULT_MAX_SEARCH_FRET = 12


class CandidatePositionFinder:

    def __init__(
        self,
        fretboard: Fretboard,
        maximum_fret: int = DEFAULT_MAX_SEARCH_FRET,
    ):
        self.fretboard = fretboard
        self.maximum_fret = maximum_fret

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
            if self._different_strings(combination)
        )

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
            position.fret <= self.maximum_fret
            for position in combination
        )