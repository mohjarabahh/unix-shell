def is_executable_file(command_name: str) -> bool:
    """
    Checks if a file is executable (i.e. command name starts with `./` or `../`).

    Example:
    >>> is_executable_file("./hello.py")
    True
    """

    return command_name.startswith("./") or command_name.startswith("../")