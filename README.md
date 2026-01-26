# Life in Weeks

A small project that visualizes lived and remaining time
based on a fixed lifespan assumption chosen by the user.

## Live demo

[Life in Weeks](https://life-in-weeks-clzz.onrender.com)

_(First load may take a few seconds due to server cold start.)_

## What this is
A deterministic visualization of time progression.

An optional time-allocation lens allows viewing remaining life
after accounting for daily obligations such as sleep and work.

## What this is not
- A death prediction tool  
- A productivity tracker  
- A motivational or behavioral app  

## Core assumptions
- Lifespan is user-defined
- Time progresses deterministically
- Time allocation is approximate and illustrative, not prescriptive
- No personalization, optimization, or tracking

## Current scope
- Birth date input
- Expected lifespan input
- Visual grid of weeks lived vs remaining
- Optional time-allocation lens (sleep, work, commute/chores)
- Aggregate awareness metrics (e.g. free time per day, free years remaining)

## Modeling notes (intentional limitations)

This project prioritizes clarity and awareness over calendar-level accuracy.

- Weeks are modeled as 52 per year for visualization purposes  
  (leap years and week 53 are not accounted for)

- Months lived are calculated at the month level only  
  (day-of-month precision is intentionally ignored)

- Time-allocation values are user-provided estimates, not measured data

The visualization represents a conceptual timeline, not a precise calendar or forecast.
