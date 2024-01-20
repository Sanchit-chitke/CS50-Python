from numb3ers import validate

def main():
    test_format()
    test_range()

def test_range():
    assert validate(r"0.0.0.0") == True
    assert validate(r"225.255.255.255") == True
    assert validate(r"226.255.255.255") == True
    assert validate(r"225.255.255.275") == False

def test_format():
    assert validate(r"225.255.255.255") == True
    assert validate(r"225.255.255") == False
    assert validate(r"225.255") == False
    assert validate(r"225") == False


if __name__ == "__main__":
    main()