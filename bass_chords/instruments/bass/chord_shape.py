from dataclasses import dataclass
from functools import cached_property
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.voicing import Voicing


@dataclass(frozen=True)
class ChordShape(Voicing):
    positions: tuple[Position, ...]

    @cached_property
    def open_strings(self) -> tuple[Position, ...]:
        return tuple(
            position
            for position in self.positions
            if position.is_open
        )

    @cached_property
    def fretted_positions(self) -> tuple[Position, ...]:
        return tuple(
            position
            for position in self.positions
            if not position.is_open
        )

    @cached_property
    def lowest_fretted_fret(self) -> int | None:

        if not self.fretted_positions:
            return None

        return min(
            position.fret
            for position in self.fretted_positions
        )

    @property
    def display_positions(self):
        return tuple(reversed(self.positions))

    def is_playable(
        self,
        bassist,
        bass,
    ):
        if self.has_repeated_strings:
            return False

        if self.lowest_fretted_fret is None:
            return True

        distance = bass.fret_distance_mm(
            self.lowest_fretted_fret,
            self.highest_fret,
        )

        return distance <= bassist.max_reach_mm
