from dataclasses import dataclass

from bass_chords.instruments.bass.position import Position


@dataclass(frozen=True)
class ChordShape:
    positions: tuple[Position, ...]