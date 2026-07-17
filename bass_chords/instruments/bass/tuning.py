from dataclasses import dataclass

from bass_chords.theory.note import Note


@dataclass(frozen=True)
class BassTuning:

    strings: tuple[Note, ...]

    @classmethod
    def standard(cls):

        return cls(
            (
                Note("E"),
                Note("A"),
                Note("D"),
                Note("G"),
            )
        )
