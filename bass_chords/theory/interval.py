from dataclasses import dataclass, field

_INTERVAL_TO_SEMITONES = {
    "1":   0,

    "b2":  1,
    "2":   2,
    "#2":  3,

    "b3":  3,
    "3":   4,

    "4":   5,
    "#4":  6,
    "b5":  6,

    "5":   7,
    "#5":  8,
    "b6":  8,

    "6":   9,
    "bb7": 9,
    "#6": 10,
    "b7": 10,

    "7":  11,

    "8": 12,

    "b9": 13,
    "9": 14,
}


@dataclass(frozen=True)
class Interval:
    name: str
    semitones: int = field(init=False)

    def __post_init__(self):
        if self.name not in _INTERVAL_TO_SEMITONES:
            raise ValueError(f"Invalid interval: {self.name}")

        object.__setattr__(
            self,
            "semitones",
            _INTERVAL_TO_SEMITONES[self.name],
        )
