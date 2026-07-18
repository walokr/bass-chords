from dataclasses import dataclass, field
from bass_chords.theory.interval import Interval
from bass_chords.theory.accidental import Accidental
from bass_chords.theory.chromatic import (
    NOTE_TO_VALUE,
    FLAT_NAMES,
    SHARP_NAMES,
)


@dataclass(frozen=True)
class Note:
    name: str
    value: int = field(init=False)

    @classmethod
    def from_value(
        cls,
        value: int,
        accidental: Accidental = Accidental.FLAT,
    ) -> "Note":

        names = (
            FLAT_NAMES
            if accidental is Accidental.FLAT
            else SHARP_NAMES
        )

        return cls(names[value % 12])

    def __post_init__(self):
        normalized = self.name.strip()

        if len(normalized) == 1:
            normalized = normalized.upper()
        else:
            normalized = normalized[0].upper() + normalized[1:]

        if normalized not in NOTE_TO_VALUE:
            raise ValueError(f"Invalid note: {self.name}")

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "value", NOTE_TO_VALUE[normalized])

    def transpose(
        self,
        interval: Interval,
        accidental: Accidental = Accidental.FLAT,
    ) -> "Note":
        """
        Returns a new note obtained by transposing this note
        by the given interval.
        """

        return Note.from_value(
            self.value + interval.semitones,
            accidental,
        )

    def __add__(self, interval: Interval) -> "Note":
        return self.transpose(interval)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Note('{self.name}')"
