from utils.is_executable_file import is_executable_file

def test_is_executable_file():
    assert is_executable_file("./hello.py") == True
    assert is_executable_file("../hello.py") == True
    assert is_executable_file(".../hello.py") == False
    assert is_executable_file("/hello.py") == False
    assert is_executable_file("hello.py") == False
