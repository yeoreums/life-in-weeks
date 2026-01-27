import os
from flask import Flask, render_template, request
from datetime import date
from model.life_model import LifeModel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

def fmt(val):
    return int(val) if isinstance(val, (int, float)) and val.is_integer() else val


@app.route("/")
def home():
    birth_str = request.args.get("birthdate")
    lifespan_str = request.args.get("lifespan")
    show = request.args.get("show") == "true"

    # --- Time Lens Inputs ---
    try:
        sleep = float(request.args.get("sleep", 0))
    except ValueError:
        sleep = 0

    try:
        work = float(request.args.get("work", 0))
    except ValueError:
        work = 0

    try:
        commute = float(request.args.get("commute", 0))
    except ValueError:
        commute = 0

    sleep = max(0, min(sleep, 24))
    work = max(0, min(work, 24))
    commute = max(0, min(commute, 24))

    overhead = min(sleep + work + commute, 24)
    free_ratio = (24 - overhead) / 24
    free_hours_per_day = fmt(round(24 - overhead, 1))
    has_lens = overhead > 0

    today = date.today()

    # -------- Birthdate --------
    if birth_str:
        birth_str = birth_str.strip()
        try:
            if len(birth_str) == 8 and birth_str.isdigit():
                birth = date(
                    int(birth_str[0:4]),
                    int(birth_str[4:6]),
                    int(birth_str[6:8]),
                )
            else:
                birth = date.fromisoformat(birth_str)
        except ValueError:
            birth = date(today.year - 30, today.month, today.day)
    else:
        birth = date(today.year - 30, today.month, today.day)

    if birth > today:
        birth = today

    # -------- Lifespan --------
    try:
        lifespan = int(lifespan_str) if lifespan_str else 90
    except ValueError:
        lifespan = 90

    lifespan = max(1, min(lifespan, 130))

    # -------- Model --------
    model = LifeModel(birth_date=birth, expected_years=lifespan)
    lived_weeks = model.lived_weeks(today)

    lived_months = (today.year - birth.year) * 12 + (today.month - birth.month)
    current_month_idx = lived_months - 1
    total_months = lifespan * 12

    # -------- Awareness Metrics (NOW SAFE) --------
    remaining_weeks = lifespan * 52 - lived_weeks
    free_weeks_remaining = int(remaining_weeks * free_ratio)
    free_years_remaining = fmt(round(free_weeks_remaining / 52, 1))

    # -------- Life Map --------
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

    return render_template(
        "index.html",
        show=show,
        birthdate=birth.isoformat(),
        lifespan=lifespan,
        lived_weeks=lived_weeks,
        lived_months=lived_months,
        current_month_idx=current_month_idx,
        total_months=total_months,
        life_map=life_map,
        sleep=fmt(sleep),
        work=fmt(work),
        commute=fmt(commute),
        free_ratio=free_ratio,
        has_lens=has_lens,
        free_hours_per_day=fmt(free_hours_per_day),
        free_years_remaining=fmt(free_years_remaining),
    )

if __name__ == "__main__":
    app.run(debug=True)