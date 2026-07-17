from enum import Enum

from bass_chords.theory.note import Note


class BassString(Enum):
    E = Note("E")
    A = Note("A")
    D = Note("D")
    G = Note("G")

    @property
    def open_note(self):
        return self.value

    def note_at(self, fret: int):
        return Note.from_value(self.open_note.value + fret)
