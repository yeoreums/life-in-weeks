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

    if birth_str:
        birth = date.fromisoformat(birth_str)
    else:
        birth = date(today.year - 30, today.month, today.day)
    
    if birth > today:
        birth = today

    if lifespan_str:
        try:
            lifespan = int(lifespan_str)
        except ValueError:
            lifespan = 90
    else:
        lifespan = 90
    
    lifespan = max(1, min(lifespan, 130))

    model = LifeModel(birth_date=birth, expected_years=lifespan)

    lived_weeks = model.lived_weeks(today)
    total_weeks = model.total_weeks()

    lived_months = model.lived_months(today)
    total_months = lifespan * 12

    current_week_index = lived_weeks - 1
    current_month_index = lived_months - 1

    return render_template(
        "index.html",
        birthdate=birth.isoformat(),
        lived_weeks=lived_weeks,
        total_weeks=total_weeks,
        lived_months=lived_months,
        total_months=total_months,
        current_week_index=current_week_index,
        current_month_index=current_month_index,
        today=today.isoformat(),
        lifespan=lifespan,
    )

if __name__ == "__main__":
    app.run(debug=True)