from datetime import date
from model.life_model import LifeModel
from visualize.text import render_week_line
from visualize.text import render_week_grid

birth = date(2000, 1, 1)
model = LifeModel(birth_date=birth, expected_years=90)

today = date(2025, 1, 1)

lived = model.lived_weeks(today)
total = model.total_weeks()
remaining = model.remaining_weeks(today)

line = render_week_line(lived=lived, total=total)
life_view = render_week_grid(lived, total)

print("Birth:", model.birth_date)
print("End:", model.end_date())
print("Lived weeks:", lived)
print("Total weeks:", total)
print("Remaining weeks:", remaining)
print(life_view)
