from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord
from bass_chords.instruments.bass.chord_shape import ChordShape
from itertools import product


class ChordFinder:

    def __init__(self, fretboard: Fretboard):
        self.fretboard = fretboard

    def find(self, chord: Chord):
        return ()

    def positions_by_note(self, chord):

        return {
            note: self.fretboard.find(note)
            for note in chord.notes
        }

    def position_combinations(self, chord: Chord):

        positions = self.positions_by_note(chord)

        return tuple(
            product(*positions.values())
        )

    def build_shapes(self, chord: Chord):

        combinations = self.position_combinations(chord)

        return tuple(
            ChordShape(positions=combination)
            for combination in combinations
        )
