from dataclasses import dataclass
from bass_chords.instruments.bass.position import Position
from functools import cached_property
from bass_chords.theory.pitch import Pitch
from bass_chords.theory.note import Note
from bass_chords.instruments.bass.bass_string import BassString


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
    def strings(self) -> tuple[BassString, ...]:

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

    @cached_property
    def fret_range(self) -> tuple[int, int]:

        return (
            self.lowest_fret,
            self.highest_fret,
        )

    @cached_property
    def lowest_pitch(self) -> Pitch:

        return min(
            self.pitches,
            key=lambda pitch: pitch.value,
        )

    @cached_property
    def highest_pitch(self) -> Pitch:

        return max(
            self.pitches,
            key=lambda pitch: pitch.value,
        )

    @cached_property
    def pitch_range(self) -> int:

        return (
            self.highest_pitch.value
            - self.lowest_pitch.value
        )

    @cached_property
    def contains_open_strings(self) -> bool:

        return any(
            position.is_open
            for position in self.positions
        )

    @cached_property
    def open_string_count(self) -> int:

        return sum(
            position.is_open
            for position in self.positions
        )

    @cached_property
    def lowest_string(self) -> BassString:

        return min(
            self.strings,
            key=lambda string: string.order,
        )

    @cached_property
    def highest_string(self) -> BassString:

        return max(
            self.strings,
            key=lambda string: string.order,
        )

    @cached_property
    def string_range(self) -> int:

        return (
            self.highest_string.order
            - self.lowest_string.order
        )
