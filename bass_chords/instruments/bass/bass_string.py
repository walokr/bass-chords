from enum import Enum

from bass_chords.theory.note import Note


class BassString(Enum):
    B = Note("B")
    E = Note("E")
    A = Note("A")
    D = Note("D")
    G = Note("G")
    C = Note("C")

    @property
    def note(self):
        return self.value

    def note_at(self, fret: int):
        return Note.from_value(self.note.value + fret)
