# bass_chords/player/player.py

from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    max_reach_mm: float = 90.0
