import sys
from subprocess import (CalledProcessError, check_call,
                        call, DEVNULL)


def _check_call_quiet(commands: list[str], *, shell: bool=False) -> None:
    try:
        check_call(commands, shell=shell)
    except CalledProcessError as error:
        sys.exit(error.returncode)
        
def format() -> None:
    _check_call_quiet(["black", "--check", "--diff", "src/", "tests/"])
    _check_call_quiet(["isort", "--check", "--diff", "src", "tests"])
    _check_call_quiet(
        ["find src/ -name *.html | xargs djhtml --tabwidth 2 --check"],
        shell=True)

def reformat() -> None:
    _check_call_quiet(["black", "src/", "tests/"])
    _check_call_quiet(["isort", "src", "tests"])
    _check_call_quiet(
        ["find src/ -name *.html | xargs djhtml --tabwidth 2 --in-place"],
        shell=True)

def lint() -> None:
    _check_call_quiet(["mypy", "src/backend/", "tests/"])
    _check_call_quiet(["flake8", "src/", "tests/"])
    _check_call_quiet(["vulture", "src/"])
    _check_call_quiet(["bandit", "-r", "src/"])

def test() -> None:
    _check_call_quiet(["pytest", "tests/", *sys.argv[1:]])

def hello():
    print("Hello")
    
def start() -> None:
    _check_call_quiet(["python", "src/backend/run.py"])