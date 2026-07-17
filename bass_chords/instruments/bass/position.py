from dataclasses import dataclass

from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.finger import Finger
from bass_chords.theory.note import Note


@dataclass(frozen=True)
class Position:
    string: BassString
    fret: int
    note: Note
    finger: Finger | None = None
