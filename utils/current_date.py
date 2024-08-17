from datetime import datetime

def current_date() -> str:
    """
    Displays the current date in a custom format.

    Example:
    >>> current_date()
    "Saturday, June 15, 2024"
    """

    return datetime.now().strftime(r"%A, %B %-d, %Y")
