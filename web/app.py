from flask import Flask
from datetime import date
from model.life_model import LifeModel
from visualize.text import render_week_grid, render_month_grid


app = Flask(__name__)

@app.route("/")
def home():
    birth = date(2000, 1, 1)
    model = LifeModel(birth_date=birth, expected_years=90)

    today = date(2025, 1, 1)

    lived = model.lived_weeks(today)
    total = model.total_weeks()

    week_grid = render_week_grid(lived, total)
    month_grid = render_month_grid(lived, total)

    return f"""
    <html>
    <head>
        <title>Life in Weeks</title>
    </head>
    <body style="background:#fafafa;">
        <div style="
        max-width: 900px;
        margin: 40px auto;
        padding: 24px;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
        background: white;
        border-radius: 8px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
        ">

        <h2>Life in Weeks</h2>
        <p style="color:#555;">
            Each square represents one week of life.
        </p>
        <pre style="line-height: 1.2;">{week_grid}</pre>

        <hr style="margin: 32px 0; border: none; border-top: 1px solid #eee;">

        <h2>Life in Months</h2>
        <p style="color:#555;">
            Each circle represents one month of life.
        </p>
        <pre style="line-height: 1.4;">{month_grid}</pre>

        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)