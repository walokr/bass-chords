from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.position import Position
from bass_chords.theory.note import Note


class Fretboard:

    def __init__(self, frets: int = 24):
        self.frets = frets

    def find(self, note: Note):

        positions = []

        for string in BassString:

            for fret in range(self.frets + 1):

                position = Position(string, fret)

                if position.note == note:
                    positions.append(position)

        return positions
