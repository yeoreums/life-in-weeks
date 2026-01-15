def render_week_line(lived: int, total: int) -> str:
    """
    Return a single-line string representing lived vs remaining weeks.
    """
    lived_symbol = "█"
    remaining_symbol = "░"
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
    
