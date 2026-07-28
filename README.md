# Bass Chords

> **Bass Chords**  
> An intelligent chord and voicing engine for bass players.

## Overview

Bass Chords is an open-source Python library that generates playable chord voicings for bass guitar.

Unlike traditional chord dictionaries, Bass Chords models three independent concepts:

- music theory,
- the instrument,
- the bassist.

By combining them, it generates chord shapes that are both musically correct and physically playable.

The project is being developed incrementally using Test-Driven Development (TDD).

---

# Current Features

## Music Theory

- Notes
- Pitches
- Intervals
- Chord formulas
- Chord parser
- Chord construction

---

## Instrument Model

### Bass

- Standard 4-string bass (E-A-D-G)
- Configurable scale length (30", 32", 34", 35", ...)
- Configurable number of frets

### Fretboard

- Position model
- String model
- ChordShape model

---

## Bassist Model

Current implementation:

- Maximum hand reach

The bassist model is independent from the instrument and will continue evolving.

---

## Chord Engine

Current capabilities:

- Position search
- Candidate position generation
- Chord shape generation
- Duplicate string elimination
- Playability evaluation
- Shape ordering

---

## Playability Model

Playability is currently evaluated using:

- duplicated string detection
- real fret spacing
- bassist maximum reach
- instrument scale length

The model is intentionally modular and will gradually incorporate additional ergonomic rules.

---

# Roadmap

## Search Engine

- SearchOptions
- MovementPreference
- Target fret search
- Candidate position pruning
- Intelligent ranking
- Voice-leading optimization

---

## Fingering

- Finger assignment
- Barre detection
- Position shifting
- Difficulty scoring

---

## Music

- Arpeggios
- Scales
- Modes
- Slash chords
- Extended chords

---

## Rendering

- ASCII diagrams
- SVG generation
- PNG generation
- PDF chord sheets

---

## Interfaces

- REST API
- Web application
- Desktop application

---

## Instruments

- Alternative tunings
- 5-string bass
- 6-string bass

---

# Technology

- Python 3.13+
- pytest
- dataclasses
- type hints

---

# Design Principles

Bass Chords follows a strict separation of responsibilities.

The project distinguishes between:

- Music Theory
- Instrument
- Bassist
- Search Strategy

Each concept evolves independently.

The implementation follows:

- Test-Driven Development
- Small evolutionary steps
- Immutable domain objects
- Clear and explicit APIs
- Simple algorithms before optimization

---

# Project Status

🚧 Active development.

The theoretical model is stable.

The first playable chord generation engine is complete.

Current development focuses on improving search intelligence through configurable search strategies and ergonomic evaluation.

---

# Philosophy

A chord is not a fingering.

A fingering depends on:

- the music,
- the instrument,
- the bassist,
- and the musical intention.

Bass Chords models each concept independently before searching for the best solution.

---

# Contributing

Suggestions, discussions, bug reports and pull requests are welcome.

---

# License

MIT License