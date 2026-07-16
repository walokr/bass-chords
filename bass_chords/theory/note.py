from dataclasses import dataclass, field


_NOTE_VALUES = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
}


@dataclass(frozen=True)
class Note:
    name: str
    value: int = field(init=False)

    def __post_init__(self):
        normalized = self.name[0].upper() + self.name[1:].lower()

        if normalized not in _NOTE_VALUES:
            raise ValueError(f"Invalid note: {self.name}")

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "value", _NOTE_VALUES[normalized])
