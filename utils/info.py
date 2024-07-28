from termcolor import colored as color_string
from utils.shell_banner import shell_banner
from utils.help import help

def info() -> str:
    """
    Displays an info message for an `info` command, which provides the shell documentation.
    """

    # create documentation sections (sections' information are sourced from `../README.md` file manually)
    overview_section = f"{color_string(' OVERVIEW ', 'black', 'on_white')}\nA simple version of UNIX Shell developed using Python language and Pytest testing framework under the Linux environment with several awesome open-source technologies. The shell can handle both built-in commands and executable files. It is not sophisticated as Bash or Zsh, but it performs similar functions.\n\nThe codebase is pretty organized, easier to maintain, and scalable as the project grows (if that happened) due to the clean file structure, clean code, and great documentation. This has been be done with modularity, best practices, documentation, documentation strings, type hinting, and unit testing, which made the codebase easier to debug and maintain, as well as, ensured code correctness."
    technologies_section = f"{color_string(' TECHNOLOGIES ', 'black', 'on_white')}\n• Python 3.10\n• PyTest 8.2\n• TermColor 2.4\n• PyFIGlet 1.0\n• TerminalTables 3.1"
    commands_section = f"{color_string(' COMMANDS ', 'black', 'on_white')}\n{help()}"
    more_details_section = f"{color_string(' MORE DETAILS ', 'black', 'on_white')}\nFor further information, you can visit `README.md` file, which is located in the project's source-code root directory."

    # group documentation sections
    documentation_message = f"{shell_banner()}\n\n{overview_section}\n\n{technologies_section}\n\n{commands_section}\n\n{more_details_section}"

    return documentation_message