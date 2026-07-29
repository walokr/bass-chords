from dataclasses import dataclass


@dataclass(frozen=True)
class SearchOptions:

    max_fret: int | None = None

    center_fret: int | None = None

    movement_preference: str = "any"

