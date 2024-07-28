from utils.split_command_line import split_command_line

def test_split_command_line():
    assert split_command_line("ls ./src -al") == { "command": "ls", "arguments": ["./src", "-al"] }
    assert split_command_line("py -m venv .venv") == {"command": "py", "arguments": ["-m", "venv", ".venv"]}