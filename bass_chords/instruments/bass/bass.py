from dataclasses import dataclass

from bass_chords.instruments.bass.bass_string import BassString


@dataclass(frozen=True)
class Bass:
    strings: tuple[BassString, ...]
    frets: int

    @classmethod
    def standard(cls):
        return cls(
            strings=(
                BassString.E,
                BassString.A,
                BassString.D,
                BassString.G,
            ),
            frets=20,
        )
