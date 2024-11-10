# tests/test_my_package
from hello import hello

def test_hello():
    assert hello("World") == "Hello, World!"
