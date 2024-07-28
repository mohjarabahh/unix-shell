from datetime import datetime

def current_time() -> str:
    """
    Displays the current time in a custom format.

    Example:
    >>> current_time()
    "1:37 AM"
    """

    current_time = datetime.now().strftime(r"%-I:%M %p")
    return current_time