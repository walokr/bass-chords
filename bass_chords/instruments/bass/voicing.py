from dataclasses import dataclass
from bass_chords.instruments.bass.position import Position
from functools import cached_property
from bass_chords.theory.pitch import Pitch
from bass_chords.theory.note import Note


@dataclass(frozen=True)
class Voicing:

    positions: tuple[Position, ...]

    @cached_property
    def pitches(self) -> tuple[Pitch, ...]:

        return tuple(
            position.pitch
            for position in self.positions
        )

    @cached_property
    def notes(self) -> tuple[Note, ...]:

        return tuple(
            pitch.note
            for pitch in self.pitches
        )

    @cached_property
    def average_fret(self) -> float:

        return (
            sum(
                position.fret
                for position in self.positions
            )
            / len(self.positions)
        )

    @cached_property
    def lowest_fret(self) -> int:

        return min(
            position.fret
            for position in self.positions
        )

    @cached_property
    def highest_fret(self) -> int:

        return max(
            position.fret
            for position in self.positions
        )

    @cached_property
    def span(self) -> int:

        return (
            self.highest_fret
            - self.lowest_fret
        )

    @cached_property
    def strings(self):

        return tuple(
            position.string
            for position in self.positions
        )

    @cached_property
    def has_repeated_strings(self) -> bool:

        return (
            len({
                position.string
                for position in self.positions
            })
            != len(self.positions)
        )
