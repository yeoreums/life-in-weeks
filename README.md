# Life in Weeks

A deterministic model that visualizes life as a finite timeline based on a user-defined lifespan.

Live demo: [https://life-in-weeks-clzz.onrender.com](https://life-in-weeks-clzz.onrender.com)

(First load may take a few seconds due to server cold start)

---

## Overview

This project models time as a finite resource and renders it as a structured timeline (weeks or months).

It includes an optional "time allocation lens" that adjusts remaining life based on daily constraints such as sleep, work, and commute.

---

## Key Features

* Birthdate and lifespan input
* Week-level and month-level life visualization
* Time allocation lens (sleep, work, commute/chores)
* Derived metrics:

  * Free time per day
  * Free years remaining
* Toggle between weeks and months view

---

## API

The application also exposes a JSON API:

**GET `/api/life`**

Example:

```
/api/life?birthdate=19900101&lifespan=90&sleep=8&work=8&commute=2
```

Response:

```json
{
  "lived_weeks": 1800,
  "free_years_remaining": 18.5,
  "free_hours_per_day": 6
}
```

---

## What this is

* A deterministic time model for visualizing life progression
* A tool for reflecting on time as a finite resource
* A system that combines a visual interface with a programmatic API for exploring time-based metrics

---

## What this is not

* A death prediction tool
* A productivity tracker
* A behavioral or recommendation system

---

## Core Assumptions

* Lifespan is user-defined
* Time progresses deterministically
* Time allocation is approximate and illustrative
* No personalization, optimization, or tracking

---

## Modeling Notes (Intentional Limitations)

This project prioritizes clarity over calendar-level precision.

* Weeks are modeled as 52 per year
  (leap years and week 53 are not included)

* Months are calculated at a coarse level
  (day-of-month precision is ignored)

* Time allocation values are user-provided estimates

This is a conceptual model, not a precise calendar or forecast.

---

## Tech Stack

* FastAPI (backend)
* Jinja2 (templating)
* Vanilla HTML/CSS/JS (frontend)
* Deployed on Render
