from pyfiglet import figlet_format

def shell_banner() -> str:
    """
    Returns an awesome text banner of the shell.
    """

    text_banner = figlet_format("UNIX Shell", "slant")
    developer_message = "Developed with 💜 using Python & Pytest by Mohammad Jarab'ah"

    return f"{text_banner} {developer_message}"
