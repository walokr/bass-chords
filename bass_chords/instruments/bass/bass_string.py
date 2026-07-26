from dataclasses import dataclass
from bass_chords.theory.pitch import Pitch
from bass_chords.theory.note import Note


@dataclass(frozen=True)
class BassString:
    pitch: Pitch

    @classmethod
    def standard_b(cls):
        return cls(Pitch(Note("B"), 0))

    @classmethod
    def standard_e(cls):
        return cls(Pitch(Note("E"), 1))

    @classmethod
    def standard_a(cls):
        return cls(Pitch(Note("A"), 1))

    @classmethod
    def standard_d(cls):
        return cls(Pitch(Note("D"), 2))

    @classmethod
    def standard_g(cls):
        return cls(Pitch(Note("G"), 2))

    @classmethod
    def standard_c(cls):
        return cls(Pitch(Note("C"), 3))

    @property
    def note(self):
        return self.pitch.note

    @property
    def order(self) -> int:

        if self == BassString.standard_e():
            return 0

        if self == BassString.standard_a():
            return 1

        if self == BassString.standard_d():
            return 2

        if self == BassString.standard_g():
            return 3

        raise ValueError("Unknown bass string")

    def pitch_at(self, fret: int) -> Pitch:
        return self.pitch.transpose(fret)

    def note_at(self, fret: int) -> Note:
        return self.pitch_at(fret).note

    def __str__(self):
        return str(self.note.name)
