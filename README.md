# Bass Chords

> **Bass Chords**  
> An intelligent chord and voicing engine for bass players.

## Overview

Bass Chords is an open-source Python library that generates playable chord voicings for bass guitar.

Unlike traditional chord dictionaries, Bass Chords evaluates every generated shape according to both the instrument geometry and the physical capabilities of the bassist, producing realistic and playable results.

The project is being developed incrementally using Test-Driven Development (TDD).

---

## Current Features

### Music Theory

- Notes
- Intervals
- Chord formulas
- Chord parser
- Chord construction

### Bass Model

- Standard 4-string bass (E-A-D-G)
- Scale length support (30", 32", 34", 35", ...)
- Fretboard model
- Position model
- String model

### Chord Engine

- Position search on the fretboard
- Chord shape generation
- Duplicate string elimination
- Shape ordering
- Playability evaluation

### Playability

Playability is currently evaluated using:

- duplicated string detection
- real fret distance
- bassist maximum hand reach
- instrument scale length

This model will evolve as more ergonomic rules are introduced.

---

## Roadmap

### Chord Engine

- Intelligent candidate position pruning
- Finger assignment
- Barre detection
- Position shifting
- Difficulty scoring
- Ranking heuristics

### Music

- Arpeggios
- Scales
- Modes
- Slash chords
- Extended chords

### Output

- Chord diagrams
- SVG generation
- PNG generation
- PDF chord sheets

### Interfaces

- REST API
- Web application
- Desktop application

### Instruments

- Alternative bass tunings
- 5-string bass
- 6-string bass

---

## Technology

- Python 3.13+
- pytest
- dataclasses
- Type hints

---

## Design Principles

The project follows a few simple principles:

- Test-Driven Development
- Small evolutionary steps
- Immutable domain objects
- Clear separation between music theory and instrument mechanics
- Keep algorithms simple before optimizing them

---

## Project Status

🚧 Active development.

The theoretical model is stable and the first generation of playable chord shapes is already working.

Current work focuses on improving the intelligence of the chord generation engine.

---

## Contributing

Suggestions, discussions, bug reports and pull requests are welcome.

---

## License

MIT License