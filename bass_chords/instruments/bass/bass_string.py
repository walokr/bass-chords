from dataclasses import dataclass
from bass_chords.theory.pitch import Pitch
from bass_chords.theory.note import Note


@dataclass(frozen=True)
class BassString:
    pitch: Pitch

    @property
    def note(self):
        return self.pitch.note

    def pitch_at(self, fret: int) -> Pitch:
        return self.pitch.transpose(fret)

    def note_at(self, fret: int) -> Note:
        return self.pitch_at(fret).note

    def __str__(self):
        return str(self.note.name)
