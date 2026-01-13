# Core Assumptions

This project treats time as a deterministic quantity.

- Lifespan is a fixed value chosen by the user
- The system date defines "today"
- No attempt is made to predict or optimize lifespan
- All views must derive from the same base life model

Interpretations such as sleep-adjusted time must layer
on top of the base model and never replace it.
