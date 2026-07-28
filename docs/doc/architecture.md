# Bass Chords

## Vision

Bass Chords is an intelligent assistant for bass players.

The project is **not** intended to be a chord dictionary.

Its purpose is to help bass players choose the most playable and musical chord voicings for every performance context.

The architecture separates four independent concepts:

- Music theory
- Instrument
- Performer
- Search strategy

This separation allows every part of the system to evolve independently.

---

# Architecture

## Music Theory

Describes music independently from any instrument.

- Note
- Pitch
- Interval
- Chord Formula
- Chord

---

## Instrument

Describes the physical characteristics of the instrument.

### Bass

- Scale Length
- Number of Frets
- Strings

### Fretboard

- Tuning
- Position
- Finger
- ChordShape

---

## Performer

Describes the physical capabilities of the bassist.

Examples:

- Maximum finger reach
- Preferred techniques
- Playing level

Current implementation:

- Player

Future ideas:

- Hand size
- Finger independence
- Barre ability
- Stretch profile

---

## Search

Describes the musical intention of a search.

Examples:

- Play around the 7th fret
- Prefer ascending movement
- Return only the best 10 shapes

Current:

- ChordFinder

Planned:

- SearchOptions
- MovementPreference

---

## Engine

Transforms musical information into playable chord shapes.

Responsibilities include:

- Candidate position generation
- Shape generation
- Playability filtering
- Ranking
- Voice leading
- Optimization

---

## Rendering

Converts chord shapes into visual representations.

Planned outputs:

- ASCII
- SVG
- PNG
- PDF

---

## API

The project will expose its functionality through a REST API.

Planned:

- FastAPI

---

# Design Principles

The project follows a strict separation of responsibilities.

Music theory should never depend on the instrument.

The instrument should never depend on the performer.

The performer should never depend on search strategies.

Search strategies should never modify music theory.

Each layer only knows what it actually needs to know.

---

# Philosophy

A chord is only one possibility.

A playable chord depends on:

- the instrument,
- the bassist,
- and the musical intention.

Bass Chords models all three independently before choosing the best solution.