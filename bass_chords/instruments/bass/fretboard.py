from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.position import Position
from bass_chords.theory.note import Note
from bass_chords.instruments.bass.bass_string import BassString


class Fretboard:

    def __init__(self, bass: Bass):
        self.bass = bass

    def find(self, note: Note):

        positions = []

        for string in self.bass.strings:

            for fret in range(self.bass.frets + 1):

                position = Position(string, fret)

                if position.note == note:
                    positions.append(position)

        return positions

    def note_at(self, string: BassString, fret: int) -> Note:
        return string.note_at(fret)
