from utils.command_not_found import command_not_found

def test_command_not_found():
    assert command_not_found("gg") == "gg: command not found!"
    assert command_not_found("echho") == "echho: command not found!"
