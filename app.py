#!/usr/bin/env python3

from os import getpid as get_pid
from os import getppid as get_ppid
from utils.change_current_directory import change_current_directory
from utils.command_not_found import command_not_found
from utils.current_date import current_date
from utils.current_time import current_time
from utils.execute_shell_command import execute_shell_command
from utils.exit import exit
from utils.help import help
from utils.info import info
from utils.is_executable_file import is_executable_file
from utils.split_command_line import split_command_line
from utils.user_prompt import user_prompt
from utils.welcome import welcome

def app():
    """The main function which serves as the entry point of the shell application."""

    print(welcome())

    while True:
        # output `user prompt`, read `command line`, and convert `command line` to python dictionary
        command_line: str = input(user_prompt()).strip()
        command_line_components: dict[str, list[str]] = split_command_line(command_line)
        command_name: str = command_line_components["command"]
        command_arguments: str = " ".join(command_line_components["arguments"])

        # select the command based on `command name`
        # - `ls` builtin command
        if "ls" == command_name:
            execute_shell_command(f"ls {command_arguments}")

        # - `mkdir` builtin command
        elif "mkdir" == command_name:
            execute_shell_command(f"mkdir {command_arguments}")

        # - `touch` builtin command
        elif "touch" == command_name:
            execute_shell_command(f"touch {command_arguments}")

        # - `pwd` builtin command
        elif "pwd" == command_name:
            execute_shell_command(f"pwd {command_arguments}")

        # - `echo` builtin command
        elif "echo" == command_name:
            execute_shell_command(f"echo {command_arguments}")

        # - `ps` builtin command
        elif "ps" == command_name:
            execute_shell_command(f"ps {command_arguments}")

        # - `clear` builtin command
        elif "clear" == command_name:
            execute_shell_command(f"clear {command_arguments}")

        # - `cd` builtin command
        elif "cd" == command_name:
            change_current_directory(command_arguments)

        # - `pid` builtin command
        elif "pid" == command_name:
            print(get_pid())

        # - `ppid` builtin command
        elif "ppid" == command_name:
            print(get_ppid())

        # - `date` builtin command
        elif "date" == command_name:
            print(current_date())

        # - `time` builtin command
        elif "time" == command_name:
            print(current_time())

        # - `info` builtin command
        elif "info" == command_name:
            print(info())

        # - `help` builtin command
        elif "help" == command_name:
            print(help())

        # - `exit` builtin command
        elif "exit" == command_name:
            print(exit())
            break

        # - empty command
        elif "" == command_name:
            continue

        # - executable files
        elif is_executable_file(command_name):
            execute_shell_command(f"{command_name} {command_arguments}")

        # - command not found
        else:
            print(command_not_found(command_name))

app()