from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord
from bass_chords.instruments.bass.chord_shape import ChordShape
from itertools import product


class ChordFinder:

    def __init__(self, fretboard: Fretboard):
        self.fretboard = fretboard

    def find(
        self,
        chord: Chord,
        bassist,
    ):
        return self.build_shapes(chord, bassist)

    def positions_by_note(self, chord):

        return {
            note: self.fretboard.find(note)
            for note in chord.notes
        }

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

        combinations = self.position_combinations(chord)

        combinations = self.filter_combinations(combinations)

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

    def filter_combinations(
        self,
        combinations,
    ):

        return tuple(
            combination
            for combination in combinations
            if len({p.string for p in combination}) == len(combination)
        )

    def candidate_positions(
        self,
        chord: Chord,
    ):
        return self.positions_by_note(chord)