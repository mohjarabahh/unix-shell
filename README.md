<h1 align="center">UNIX Shell</h1>

## Overview
A simple version of UNIX Shell developed using Python programming language and Pytest framework, under a Linux environment, with several awesome [open-source technologies](#technologies). The shell can handle both [built-in commands](#shell-commands) and executable files. It is not sophisticated as *Bash* or *Zsh*, but it performs similar functions.

## Preview
![UNIX Shell Project Preview](./.github/assets/preview-1.png)

## Demo
![UNIX Shell Project Demo](./.github/assets/demo.gif)

## Shell Commands
| Command | Description |
| :- | :- |
| `ls` | Lists files and directories in the current location. |
| `cd` | Changes the current working directory. |
| `pwd` | Displays full pathname of the current working directory |
| `mkdir` | Creates a new directory. |
| `touch` | Creates an empty file or updates the timestamp of an existing file. |
| `clear` | Clears the terminal screen. |
| `date` | Displays the current date. |
| `time` | Displays the current time. |
| `ps` | Displays information about currently running processes. |
| `echo` | Prints text or variables to the terminal. |
| `pid` | Displays the shell Process ID (PID). |
| `ppid` | Displays the shell Parent Process ID (PPID). |
| `info` | Provides the project documentation. |
| `help` | Provides information and help about shell commands. |
| `exit` | Terminates the current shell session. |
| Executable Files | Executes executable files located in the current directory (`./`) or the parent directory (`../`). |
<!-- information of commands and their description are sourced from `/utils/help.py` file manually -->

## Technologies
- [Python 3.10](https://github.com/python/cpython)
- [PIP 22.0](https://pypi.org/project/pip)
- [PyTest 8.2](https://github.com/pytest-dev/pytest)
- [TermColor 2.4](https://github.com/termcolor/termcolor)
- [PyFIGlet 1.0](https://github.com/pwaller/pyfiglet)
- [TerminalTables 3.1](https://github.com/matthewdeanmartin/terminaltables)

## Setup
- Create a virtual environment.
    ```sh
    python3.10 -m venv .venv
    ```

- Activate the virtual environment.
    ```sh
    source .venv/bin/activate
    ```

- Install dependencies.
    ```sh
    pip install -r requirements.txt
    ```

- Make the `app.py` file executable.
    ```sh
    chmod +x app.py
    ```

- Run the shell.
    ```sh
    ./app.py
    ```

## Tests
- Activate the virtual environment.
    ```sh
    source .venv/bin/activate
    ```

- Install development dependencies.
    ```sh
    pip install -r requirements-dev.txt
    ```

- Run Pytest.
    ```sh
    pytest -v
    ```

## License
This project is licensed under the [MIT License](./LICENSE).
