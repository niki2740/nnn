# tests/test_my_package.py
from my_package import hello

def test_hello():
    assert hello("World") == "Hello, World!"