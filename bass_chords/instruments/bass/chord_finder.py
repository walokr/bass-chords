from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord


class ChordFinder:

    def __init__(self, fretboard: Fretboard):
        self.fretboard = fretboard

    def find(self, chord: Chord):
        return ()
