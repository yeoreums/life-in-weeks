from dataclasses import dataclass
from datetime import date


def weeks_between(start: date, end: date) -> int:
    """
    Return the number of FULL weeks between two dates.

    Rules:
    - If end is before start, return 0.
    - Only count complete weeks (floor).
    """
    # TODO: implement
    if end < start:
        return 0
    days = (end - start).days
    weeks = days // 7
    return weeks


@dataclass(frozen=True)
class LifeModel:
    birth_date: date
    expected_years: int

    def end_date(self) -> date:
        """
        Return the date when the expected lifespan ends.
        Example: birth_date + expected_years.
        """
        # TODO: implement
        birth = self.birth_date
        years = self.expected_years
        
        end_year = birth.year + years
        end_month = birth.month
        end_day = birth.day
        return date(end_year, end_month, end_day)

    def lived_weeks(self, today: date | None = None) -> int:
        """
        Weeks lived from birth_date to today.
        """
        # TODO: implement using weeks_between
        pass

    def total_weeks(self) -> int:
        """
        Total weeks in the expected lifespan.
        """
        # TODO: implement using weeks_between
        pass

    def remaining_weeks(self, today: date | None = None) -> int:
        """
        Remaining weeks = total - lived (never negative).
        """
        # TODO: implement
        pass
