def split_command_line(command_line: str) -> dict[str, list[str]]:
    """
    Converts `command line` (input by user) to a python dictionary contains `command (value: str)` and `arguments (value: list[str])` keys.

    Example:
    >>> split_command_line("ls ./src -al")
    {
        "command": "ls",
        "arguments": ["./src", "-al"]
    }
    """

    # split command line into list of strings based on single white space (i.e. ` `)
    command_line_list = command_line.split(" ")

    # convert command line to python dictionary contains `command` (str) and `arguments` (list[str]) keys
    command_line_components = {
        "command": command_line_list[0],
        "arguments": command_line_list[1:]
    }

    return command_line_components