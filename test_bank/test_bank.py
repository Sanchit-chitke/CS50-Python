from bank import value

def main():
    test_hello_greeting()
    test_return_20()
    test_return_100()


def test_hello_greeting():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HellO") == 0

def test_return_20():
    assert value("hi") == 20
    assert value("hey how are you") == 20

def test_return_100():
    assert value("Whats your name?") == 100
    assert value("good morning to you") == 100


if __name__ == "__main__":
    main()