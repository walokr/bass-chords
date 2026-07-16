from dataclasses import dataclass, field
from bass_chords.theory.chromatic import NOTE_NAMES, NOTE_TO_VALUE


@dataclass(frozen=True)
class Note:
    name: str
    value: int = field(init=False)
    
    @classmethod
    def from_value(cls, value: int):
        return cls(NOTE_NAMES["flat"][value % 12])
    
    def __post_init__(self):
        @classmethod
        def from_value(cls, value: int):
            return cls(NOTE_NAMES["flat"][value % 12])
        normalized = self.name.strip()

        if len(normalized) == 1:
            normalized = normalized.upper()
        else:
            normalized = normalized[0].upper() + normalized[1:]

        if normalized not in NOTE_TO_VALUE:
            raise ValueError(f"Invalid note: {self.name}")

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "value", NOTE_TO_VALUE[normalized])

