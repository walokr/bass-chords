from bass_chords.instruments.bass.bass_string import BassString
from bass_chords.instruments.bass.position import Position
from bass_chords.instruments.bass.voicing import Voicing
from bass_chords.instruments.bass.voicing_evaluator import VoicingEvaluator


def test_score_returns_float():

    evaluator = VoicingEvaluator()

    voicing = Voicing((
        Position(BassString.standard_e(), 3),
        Position(BassString.standard_a(), 2),
        Position(BassString.standard_d(), 5),
    ))

    score = evaluator.score(voicing)

    assert isinstance(score, float)


def test_pitch_range():

    voicing = Voicing((
        Position(BassString.standard_e(), 3),   # G1
        Position(BassString.standard_a(), 2),   # B1
        Position(BassString.standard_d(), 5),   # G2
    ))

    assert voicing.pitch_range == 12
