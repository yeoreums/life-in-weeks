import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import date
from model.life_model import LifeModel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


def fmt(val):
    return int(val) if isinstance(val, (int, float)) and float(val).is_integer() else val


# shared function (no duplication)
def parse_birth(birthdate: str, today: date) -> date:
    s = birthdate.strip()
    try:
        if len(s) == 8 and s.isdigit():
            return date(int(s[0:4]), int(s[4:6]), int(s[6:8]))
        elif s:
            return date.fromisoformat(s)
    except ValueError:
        pass
    return date(today.year - 30, today.month, today.day)


# ---------------------------
# HTML PAGE
# ---------------------------
@app.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    birthdate: str = "",
    lifespan: int = 90,
    show: str = "",
    view: str = "weeks",
    sleep: float = 0,
    work: float = 0,
    commute: float = 0,
):
    show_flag = show == "true"

    sleep = max(0, min(sleep, 24))
    work = max(0, min(work, 24))
    commute = max(0, min(commute, 24))

    overhead = min(sleep + work + commute, 24)
    free_ratio = (24 - overhead) / 24
    free_hours_per_day = fmt(round(24 - overhead, 1))
    has_lens = overhead > 0

    today = date.today()

    # use shared function
    birth = parse_birth(birthdate, today)

    if birth > today:
        birth = today

    lifespan = max(1, min(lifespan, 130))

    model = LifeModel(birth_date=birth, expected_years=lifespan)
    lived_weeks = model.lived_weeks(today)

    lived_months = (today.year - birth.year) * 12 + (today.month - birth.month)
    current_month_idx = lived_months - 1
    total_months = lifespan * 12

    remaining_weeks = lifespan * 52 - lived_weeks
    free_weeks_remaining = int(remaining_weeks * free_ratio)
    free_years_remaining = fmt(round(free_weeks_remaining / 52, 1))

    life_map = []
    for year_idx in range(lifespan):
        year_weeks = []
        for week_in_year in range(52):
            abs_week = (year_idx * 52) + week_in_year
            year_weeks.append({
                "lived": abs_week < lived_weeks,
                "current": abs_week == lived_weeks - 1,
                "week_num": week_in_year + 1,
            })
        life_map.append(year_weeks)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "show": show_flag,
            "view": view,
            "birthdate": birth.isoformat(),
            "lifespan": lifespan,
            "lived_weeks": lived_weeks,
            "lived_months": lived_months,
            "current_month_idx": current_month_idx,
            "total_months": total_months,
            "life_map": life_map,
            "sleep": fmt(sleep),
            "work": fmt(work),
            "commute": fmt(commute),
            "free_ratio": free_ratio,
            "has_lens": has_lens,
            "free_hours_per_day": free_hours_per_day,
            "free_years_remaining": free_years_remaining,
        },
    )


# ---------------------------
# API
# ---------------------------
@app.get("/api/life")
async def get_life(
    birthdate: str = "",
    lifespan: int = 90,
    sleep: float = 0,
    work: float = 0,
    commute: float = 0,
):
    today = date.today()

    sleep = max(0, min(sleep, 24))
    work = max(0, min(work, 24))
    commute = max(0, min(commute, 24))

    birth = parse_birth(birthdate, today)

    if birth > today:
        birth = today

    lifespan = max(1, min(lifespan, 130))

    model = LifeModel(birth_date=birth, expected_years=lifespan)
    lived_weeks = model.lived_weeks(today)

    overhead = min(sleep + work + commute, 24)
    free_ratio = (24 - overhead) / 24
    free_hours_per_day = round(24 - overhead, 1)

    remaining_weeks = lifespan * 52 - lived_weeks
    free_weeks_remaining = int(remaining_weeks * free_ratio)
    free_years_remaining = round(free_weeks_remaining / 52, 1)

    return {
        "lived_weeks": lived_weeks,
        "free_years_remaining": free_years_remaining,
        "free_hours_per_day": free_hours_per_day,
    }


# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web.app:app", host="0.0.0.0", port=8000, reload=True)