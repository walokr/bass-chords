from dataclasses import dataclass

from bass_chords.instruments.bass.bass_string import BassString


@dataclass(frozen=True)
class Bass:
    strings: tuple[BassString, ...]
    frets: int