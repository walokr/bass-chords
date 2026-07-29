from bass_chords.search.search_options import SearchOptions


def test_default_values():

    options = SearchOptions()

    assert options.max_fret is None
    assert options.center_fret is None
    assert options.movement_preference == "any"