def command_not_found(command_name: str) -> str:
    """
    Displays an error message when a user input a command that is not defined in the shell source-code.

    Example:
    >>> command_not_found("gg")
    "gg: command not found!"
    """

    return f"{command_name}: command not found!"