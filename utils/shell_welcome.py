from termcolor import colored as color_string
from utils.shell_banner import shell_banner

def shell_welcome() -> str:
    """
    Displays the shell welcome message with an awesome text banner, and a note for `help` command.
    """

    return f"{shell_banner()}\n\nNote: Type `{color_string('help', 'yellow')}` to display an information and help about shell commands."
