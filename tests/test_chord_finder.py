# import os
# import sys

# # 1. ENCONTRAR LA RAÍZ DEL PROYECTO (D:\wal\prog\bass-chords)
# # __file__ es "D:\wal\prog\bass-chords\tests\test_chord_finder.py"
# # El primer dirname da "...\tests", el segundo da "...\bass-chords"
# raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # 2. AGREGAR LA RAÍZ AL PATH DE PYTHON INMEDIATAMENTE
# if raiz_proyecto not in sys.path:
#     sys.path.insert(0, raiz_proyecto)


from bass_chords.instruments.bass.bass import Bass
from bass_chords.instruments.bass.chord_finder import ChordFinder
from bass_chords.instruments.bass.chord_shape import ChordShape
from bass_chords.instruments.bass.fretboard import Fretboard
from bass_chords.theory.chord import Chord
from bass_chords.theory.chord import Note


def test_create_chord_finder():

    fretboard = Fretboard(Bass.standard())

    finder = ChordFinder(fretboard)

    assert finder.fretboard is fretboard


def test_find_returns_tuple():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.find(
        Chord.parse("C")
    )

    assert isinstance(shapes, tuple)


def test_find_returns_chord_shapes():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.find(
        Chord.parse("C")
    )

    assert all(
        isinstance(shape, ChordShape)
        for shape in shapes
    )


def test_positions_by_note():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    positions = finder.positions_by_note(
        Chord.parse("C")
    )

    assert positions.keys() == {
        Note("C"),
        Note("E"),
        Note("G"),
    }

    assert len(positions[Note("C")]) > 0
    assert len(positions[Note("E")]) > 0
    assert len(positions[Note("G")]) > 0


def test_position_combinations():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    combinations = finder.position_combinations(
        Chord.parse("C")
    )

    assert isinstance(combinations, tuple)

    assert len(combinations) > 0

    assert all(
        len(combination) == 3
        for combination in combinations
    )


def test_build_shapes_returns_tuple():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.build_shapes(
        Chord.parse("C")
    )

    assert isinstance(shapes, tuple)


def test_build_shapes_returns_at_least_one_shape():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.build_shapes(
        Chord.parse("C")
    )

    assert len(shapes) > 0


def test_build_shapes_uses_different_strings():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.build_shapes(
        Chord.parse("C")
    )

    assert all(
        len({position.string for position in shape.positions})
        == len(shape.positions)
        for shape in shapes
    )


def test_shapes_are_sorted():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.build_shapes(
        Chord.parse("C")
    )

    assert shapes == tuple(
        sorted(
            shapes,
            key=lambda s: (
                s.span,
                s.lowest_fretted_fret,
            ),
        )
    )


def test_find_returns_at_least_one_shape():

    finder = ChordFinder(
        Fretboard(Bass.standard())
    )

    shapes = finder.find(
        Chord.parse("C")
    )

    assert len(shapes) > 0

# if __name__ == "__main__":
#     test_build_shapes()
