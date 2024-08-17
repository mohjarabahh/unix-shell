from os import system as execute_command

def execute_shell_command(command_line: str) -> None:
    """
    Executes a UNIX-like shell commands (i.e. Bash commands).

    Example:
    >>> execute_shell_command("ls")
    The shell output would be: `app.py  src  tests README.md`
    """

    execute_command(command_line)
