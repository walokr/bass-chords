from dataclasses import dataclass

from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.theory.note import Note
from bass_chords.theory.pitch import Pitch


@dataclass(frozen=True)
class Bass:
    strings: tuple[BassString, ...]
    frets: int

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
        )