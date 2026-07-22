from dataclasses import dataclass

from bass_chords.theory.note import Note


@dataclass(frozen=True)
class Pitch:
    note: Note
    octave: int

    @property
    def value(self) -> int:
        return self.octave * 12 + self.note.value

    def transpose(self, semitones: int) -> "Pitch":
        value = self.value + semitones

        return Pitch(
            note=Note.from_value(value),
            octave=value // 12,
        )

    def __str__(self):
        return f"{self.note}{self.octave}"
