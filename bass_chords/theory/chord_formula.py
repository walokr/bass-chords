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
