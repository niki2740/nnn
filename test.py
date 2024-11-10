from hello import hello, goodbye

def test_hello():
    assert hello("World") == "Привет, World!"

def test_goodbye():
    assert goodbye("Python") == "До свидания, Python!"
