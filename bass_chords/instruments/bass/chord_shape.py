from dataclasses import dataclass
from functools import cached_property
from bass_chords.instruments.bass.position import Position


@dataclass(frozen=True)
class ChordShape:
    positions: tuple[Position, ...]

    @cached_property
    def lowest_fret(self) -> int:
        return min(position.fret for position in self.positions)

    @cached_property
    def highest_fret(self) -> int:
        return max(position.fret for position in self.positions)

    @cached_property
    def span(self) -> int:
        return self.highest_fret - self.lowest_fret

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

    @property
    def open_string_count(self):
        return sum(
            position.is_open
            for position in self.positions
        )

    @property
    def has_repeated_strings(self):

        return (
            len({p.string for p in self.positions})
            != len(self.positions)
        )

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
