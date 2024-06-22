from terminaltables import SingleTable as create_table

def help() -> str:
    """
    Displays a help message for a `help` command, which provides an information and help about shell commands.
    """

    table_data = (
        ("Command", "Description"),
        ("ls", "Lists files and directories in the current location."),
        ("cd", "Changes the current working directory."),
        ("pwd", "Displays full pathname of the current working directory"),
        ("mkdir", "Creates a new directory."),
        ("touch", "Creates an empty file or updates the timestamp of an existing file."),
        ("clear", "Clears the terminal screen."),
        ("date", "Displays the current date."),
        ("time", "Displays the current time."),
        ("ps", "Displays information about currently running processes."),
        ("echo", "Prints text or variables to the terminal"),
        ("pid", "Displays the shell Process ID (PID)."),
        ("ppid", "Displays the shell Parent Process ID (PPID)."),
        ("info", "Provides the project documentation."),
        ("help", "Provides information and help about shell commands."),
        ("exit", "Terminates the current shell session."),
        ("Executable Files", "Executes executable files located in the current directory (./) or the parent directory (../).")
    )

    table_instance = create_table(table_data)
    table_instance.inner_row_border = True

    return table_instance.table