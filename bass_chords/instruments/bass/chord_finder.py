from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord
from bass_chords.instruments.bass.chord_shape import ChordShape
from itertools import product
from bass_chords.instruments.bass.candidate_position_finder import CandidatePositionFinder
from bass_chords.instruments.bass.candidate_combination_filter import CandidateCombinationFilter


class ChordFinder:

    def __init__(self, fretboard: Fretboard):

        self.fretboard = fretboard
        self.candidate_position_finder = CandidatePositionFinder(
            fretboard
        )
        self.candidate_combination_filter = CandidateCombinationFilter()

    def find(
        self,
        chord: Chord,
        bassist,
    ):
        return self.build_shapes(chord, bassist)

    
    def position_combinations(self, chord: Chord):

        positions = self.candidate_positions(chord)

        return tuple(
            product(*positions.values())
        )

    def build_shapes(
        self,
        chord: Chord,
        bassist,
    ):

        combinations = self.candidate_position_finder.find(chord)
        
        shapes = tuple(
            ChordShape(positions=combination)
            for combination in combinations
        )

        shapes = self.filter_shapes(
            shapes,
            bassist,
        )

        return self.sort_shapes(shapes)

    def filter_shapes(
        self,
        shapes: tuple[ChordShape, ...],
        bassist,
    ) -> tuple[ChordShape, ...]:

        return tuple(
            shape
            for shape in shapes
            if shape.is_playable(
                bassist,
                self.fretboard.bass,
            )
        )

    def sort_shapes(
        self,
        shapes: tuple[ChordShape, ...],
    ) -> tuple[ChordShape, ...]:

        return tuple(
            sorted(
                shapes,
                key=lambda shape: (
                    shape.span,
                    shape.lowest_fretted_fret,
                ),
            )
        )
