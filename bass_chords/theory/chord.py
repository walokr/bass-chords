from dataclasses import dataclass
from functools import cached_property

from bass_chords.theory.chord_formula import ChordFormula
from bass_chords.theory.note import Note
import re


@dataclass(frozen=True)
class Chord:
    root: Note
    symbol: str

    @cached_property
    def formula(self) -> ChordFormula:
        return ChordFormula(self.symbol)

    @cached_property
    def notes(self) -> tuple[Note, ...]:
        return tuple(
            self.root + interval
            for interval in self.formula.intervals
        )

    @classmethod
    def parse(cls, text: str) -> "Chord":
        """
        Parse a chord symbol.

        Examples:
            F7
            Bbmaj7
            C#m7
            C
        """

        match = re.fullmatch(
            r"([A-G])([b#]?)(.*)",
            text.strip(),
        )

        if match is None:
            raise ValueError(f"Invalid chord: {text}")

        note_name = match.group(1) + match.group(2)
        symbol = match.group(3)

        return cls(
            root=Note(note_name),
            symbol=symbol,
        )
