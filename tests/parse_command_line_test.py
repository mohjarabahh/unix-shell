from utils.parse_command_line import parse_command_line

def test_parse_command_line():
    assert parse_command_line("ls ./src -al") == {
        "command": "ls",
        "arguments": ["./src", "-al"]
    }

    assert parse_command_line("py -m venv .venv") == {
        "command": "py",
        "arguments": ["-m", "venv", ".venv"]
    }
