from flask import Flask
from datetime import date
from model.life_model import LifeModel
from visualize.text import render_week_grid


app = Flask(__name__)

@app.route("/")
def home():
    birth = date(2000, 1, 1)
    model = LifeModel(birth_date=birth, expected_years=90)

    today = date(2025, 1, 1)

    lived = model.lived_weeks(today)
    total = model.total_weeks()

    grid = render_week_grid(lived, total)

    return f"<pre>{grid}</pre>"

if __name__ == "__main__":
    app.run(debug=True)