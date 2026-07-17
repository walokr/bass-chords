from dataclasses import dataclass, field

from bass_chords.theory.interval import Interval


_CHORD_FORMULAS = {
    "": ("1", "3", "5"),
    "m": ("1", "b3", "5"),
    "7": ("1", "3", "5", "b7"),
    "maj7": ("1", "3", "5", "7"),
    "m7": ("1", "b3", "5", "b7"),
    "dim": ("1", "b3", "b5"),
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
