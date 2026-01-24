# Life in Weeks

A small project that visualizes lived and remaining time
based on a fixed lifespan assumption chosen by the user.

## What this is
A deterministic visualization of time progression.

## What this is not
- A death prediction tool
- A productivity tracker
- A motivational or behavioral app

## Core assumptions
- Lifespan is user-defined
- Time progresses deterministically
- No personalization or optimization

## MVP scope
- Birth date input
- Expected lifespan input
- Visual grid of weeks lived vs remaining

## Planned extensions
- Optional time-allocation lenses (sleep, eating)

## Modeling notes (MVP limitations)

This project intentionally prioritizes clarity and simplicity over calendar-level accuracy.

- Weeks are modeled as 52 per year for visualization purposes  
  (leap years and week 53 are not accounted for)

- Months lived are calculated at the month level only  
  (day-of-month precision is intentionally ignored)

- The visualization represents a deterministic timeline, not a precise calendar mapping

These tradeoffs are deliberate for the MVP and may be refined in future iterations.
