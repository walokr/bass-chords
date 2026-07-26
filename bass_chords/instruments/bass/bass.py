from dataclasses import dataclass
from math import pow
from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note
from bass_chords.theory.pitch import Pitch


@dataclass(frozen=True)
class Bass:
    strings: tuple[BassString, ...]
    frets: int
    scale_length: int = 34

    @classmethod
    def standard(cls):
        return cls(
            strings=(
                BassString(Pitch(Note("E"), 1)),
                BassString(Pitch(Note("A"), 1)),
                BassString(Pitch(Note("D"), 2)),
                BassString(Pitch(Note("G"), 2)),
            ),
            frets=20,
            scale_length=34,
        )

    def fret_position(self, fret: int) -> float:
        """
        Distancia desde la cejuela hasta el traste, en pulgadas.
        """

        return self.scale_length * (
            1 - 1 / pow(2, fret / 12)
        )

    def fret_distance(
        self,
        first: int,
        last: int,
    ) -> float:

        return abs(
            self.fret_position(last)
            - self.fret_position(first)
        )

    def fret_distance_mm(
        self,
        first: int,
        last: int,
    ) -> float:
        return self.fret_distance(first, last) * 25.4
