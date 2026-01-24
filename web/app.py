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

@app.route("/")
def home():
    birth_str = request.args.get("birthdate")
    lifespan_str = request.args.get("lifespan")

    today = date.today()

    # -------- Birthdate Logic (bug-fixed) --------
    if birth_str:
        birth_str = birth_str.strip()
        try:
            # Allow YYYYMMDD (e.g. 19900101)
            if len(birth_str) == 8 and birth_str.isdigit():
                birth = date(
                    int(birth_str[0:4]),
                    int(birth_str[4:6]),
                    int(birth_str[6:8]),
                )
            else:
                # Allow YYYY-MM-DD
                birth = date.fromisoformat(birth_str)
        except ValueError:
            birth = date(today.year - 30, today.month, today.day)
    else:
        birth = date(today.year - 30, today.month, today.day)

    if birth > today:
        birth = today

    # -------- Lifespan Logic --------
    try:
        lifespan = int(lifespan_str) if lifespan_str else 90
    except ValueError:
        lifespan = 90

    lifespan = max(1, min(lifespan, 130))

    # -------- Model --------
    model = LifeModel(birth_date=birth, expected_years=lifespan)

    lived_weeks = model.lived_weeks(today)

    # -------- Month Stats (kept exactly as-is) --------
    lived_months = (today.year - birth.year) * 12 + (today.month - birth.month)
    current_month_idx = lived_months - 1
    total_months = lifespan * 12

    # -------- Life Map (Weeks grouped by year) --------
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

    # -------- Render --------
    return render_template(
        "index.html",
        birthdate=birth.isoformat(),
        lifespan=lifespan,
        lived_weeks=lived_weeks,
        lived_months=lived_months,
        current_month_idx=current_month_idx,
        total_months=total_months,
        life_map=life_map,
    )

if __name__ == "__main__":
    app.run(debug=True)
