from dataclasses import dataclass
from functools import cached_property

from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.finger import Finger
from bass_chords.theory.note import Note


@dataclass(frozen=True)
class Position:
    string: BassString
    fret: int
    finger: Finger | None = None

    @cached_property
    def note(self) -> Note:
        return self.string.note_at(self.fret)

    @property
    def is_open(self) -> bool:
        return self.fret == 0

    def __str__(self):

        text = f"{self.string.name}{self.fret} {self.note}"

        if self.finger is not None:
            text += f" ({self.finger})"

        return text
