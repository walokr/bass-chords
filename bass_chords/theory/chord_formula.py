#
# Chord formula conventions
#
# This project follows the modern jazz harmony convention described by
# Mark Levine (The Jazz Theory Book) and commonly adopted by Berklee.
#
# Extended chords are represented by their complete theoretical formula.
#
# Examples:
#   9   = 1 3 5 b7 9
#   11  = 1 3 5 b7 9 11
#   13  = 1 3 5 b7 9 11 13
#
# These formulas describe the chord structure, not a practical voicing.
# In performance, musicians often omit the 5th, the 11th, or other tones
# depending on the musical context.
#
from dataclasses import dataclass, field

from bass_chords.theory.interval import Interval

_CHORD_FORMULAS = {
    #
    # Triads
    #
    "": ("1", "3", "5"),
    "m": ("1", "b3", "5"),
    "dim": ("1", "b3", "b5"),
    "aug": ("1", "3", "#5"),

    #
    # Suspended
    #
    "sus2": ("1", "2", "5"),
    "sus4": ("1", "4", "5"),

    #
    # Sixths
    #
    "6": ("1", "3", "5", "6"),
    "m6": ("1", "b3", "5", "6"),

    #
    # Sevenths
    #
    "7": ("1", "3", "5", "b7"),
    "maj7": ("1", "3", "5", "7"),
    "m7": ("1", "b3", "5", "b7"),
    "mMaj7": ("1", "b3", "5", "7"),
    "dim7": ("1", "b3", "b5", "bb7"),
    "m7b5": ("1", "b3", "b5", "b7"),

    #
    # Added Tone
    #
    "add2": ("1", "2", "3", "5"),
    "add4": ("1", "3", "4", "5"),
    "add9": ("1", "3", "5", "9"),
    "add11": ("1", "3", "5", "11"),
    "add13": ("1", "3", "5", "13"),

    #
    # Extended
    #
    "9": ("1", "3", "5", "b7", "9"),
    "maj9": ("1", "3", "5", "7", "9"),
    "m9": ("1", "b3", "5", "b7", "9"),

    #
    # 11th
    #
    "11": ("1", "3", "5", "b7", "9", "11"),

    #
    # 11th
    #
    "13": ("1", "3", "5", "b7", "9", "11", "13"),

    #
    # Altered
    #
    "7b5": ("1", "3", "b5", "b7"),
    "7#5": ("1", "3", "#5", "b7"),
    "7b9": ("1", "3", "5", "b7", "b9"),
    "7#9": ("1", "3", "5", "b7", "#9"),
    "7#11": ("1", "3", "5", "b7", "9", "#11"),
    "7b13": ("1", "3", "5", "b7", "9", "b13"),
    "maj11": ("1", "3", "5", "7", "9", "11"),
    "maj13": ("1", "3", "5", "7", "9", "11", "13"),
    "m11": ("1", "b3", "5", "b7", "9", "11"),
    "m13": ("1", "b3", "5", "b7", "9", "11", "13"),
}


@dataclass(frozen=True)
class ChordFormula:
    symbol: str
    intervals: tuple[Interval, ...] = field(init=False)

    def __post_init__(self):
        if self.symbol not in _CHORD_FORMULAS:
            raise ValueError(f"Invalid chord formula: {self.symbol}")

        object.__setattr__(
            self,
            "intervals",
            tuple(
                Interval(name)
                for name in _CHORD_FORMULAS[self.symbol]
            ),
        )
