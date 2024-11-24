def validate_year(year: int) -> None:
    if year and year < 0:
        raise ValueError(f"Year must be a non-negative integer.")