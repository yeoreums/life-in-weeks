def render_week_line(
    lived: int,
    total: int,
    lived_symbol: str = "■",
    remaining_symbol: str = "□",
) -> str:
    """
    Return a single-line string representing lived vs remaining weeks.
    """
    lived_part = lived_symbol * lived
    remaining_part = (total - lived) * remaining_symbol
    return lived_part + remaining_part


def render_week_grid(lived: int, total: int, per_row: int = 52) -> str:
    """
    Return a multi-line string showing life in weeks.
    """
    line = render_week_line(lived, total)

    rows = []
    for i in range(0, len(line), per_row):
        chunk = line[i:i + per_row]
        rows.append(chunk)
        
    return "\n".join(rows)
    
def render_month_grid(
    lived_weeks: int,
    total_weeks: int,
    per_row: int = 12,
) -> str:
    """
    Return a month-based life grid.
    Each circle represents one month.
    """
    lived_months = lived_weeks // 4
    total_months = total_weeks // 4

    lived_symbol = "○"
    remaining_symbol = "●"

    line = (
        lived_symbol * lived_months
        + remaining_symbol * (total_months - lived_months)
    )

    rows = []
    for i in range(0, total_months, per_row):
        rows.append(line[i : i + per_row])

    return "\n".join(rows)
