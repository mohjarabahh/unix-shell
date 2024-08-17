def parse_command_line(command_line: str) -> dict[str, str | list[str]]:
    """
    Parses a command line string into a dictionary contains command (`str`) and its arguments (`list[str]`).

    Example:
    >>> parse_command_line("ls ./src -al")
    {
        "command": "ls",
        "arguments": ["./src", "-al"]
    }
    """

    # split command line into list of strings
    command_line_list = command_line.split(" ")

    # convert command line list to dictionary
    command_line_components = {
        "command": command_line_list[0],
        "arguments": command_line_list[1:]
    }

    return command_line_components
