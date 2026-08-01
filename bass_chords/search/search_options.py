from dataclasses import dataclass

DEFAULT_MAX_SEARCH_FRET = 24


@dataclass(frozen=True)
class SearchOptions:

    min_fret: int = 0

    max_fret: int = DEFAULT_MAX_SEARCH_FRET

    center_fret: int | None = None

    movement_preference: str = "any"
