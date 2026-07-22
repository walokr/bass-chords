from dataclasses import dataclass

from bass_chords.theory.note import Note


@dataclass(frozen=True)
class Pitch:
    note: Note
    octave: int

    @property
    def value(self) -> int:
        return self.octave * 12 + self.note.value

    def __str__(self) -> str:
        return f"{self.note}{self.octave}"