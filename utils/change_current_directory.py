from os import chdir as change_working_directory
from os.path import exists as is_directory_exists

def change_current_directory(directory_path: str) -> None:
    """
    Changes the current working directory of the shell. Displays error message if directory path does not exist!

    Example:
    >>> change_current_directory("non/exist/directory")
    "sorry, the directory `non/exist/directory` does not exist."
    """

    if is_directory_exists(directory_path):
        change_working_directory(directory_path)
    else:
        print(f"sorry, the directory `{directory_path}` does not exist.")