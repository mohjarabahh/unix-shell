from datetime import datetime

def current_date() -> str:
    """
    Displays the current date in a custom format.

    Example:
    >>> current_date()
    "Saturday, June 15, 2024"
    """

    current_date = datetime.now().strftime(r"%A, %B %-d, %Y")
    return current_date