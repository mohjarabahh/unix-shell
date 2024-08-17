from getpass import getuser as get_username
from socket import gethostname as get_hostname
from os import getcwd as get_cwd
from termcolor import colored as color_string

def user_prompt() -> str:
    """
    Displays the user prompt of the shell in format of `user@hostname:current/working/directory$ ` with a colored parts.

    Example:
    >>> user_prompt()
    "mohammad@jarabah:/home$ "
    """

    # obtain username, hostname, and current working directory from the user machine
    username = get_username()
    hostname = get_hostname()
    current_working_directory = get_cwd()

    # colorize text of user prompt
    green_side = color_string(username + "@" + hostname, "green")
    magenta_side = color_string(current_working_directory, "magenta")

    return f"{green_side}:{magenta_side}$ "
