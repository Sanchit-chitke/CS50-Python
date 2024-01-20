from plates import is_valid

def main():
    # call the test functions
    test_max_min_plate()
    test_start_with_two_letters()
    test_number_middle()
    test_first_number_zero()
    test_punctuation()

# checking the length of the plate min and max
def test_max_min_plate():
    assert is_valid("cs50") == True
    assert is_valid("MH14") == True
    assert is_valid("MH") == True
    assert is_valid("MH1412") == True
    assert is_valid("M") == False

# A valid plate must start with two letter 
def test_start_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") ==  False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_number_middle():
    assert is_valid("MH1412") == True
    assert is_valid("MH14A") == False

def test_first_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("MH04") == False

def test_punctuation():
    assert is_valid("MH.12,") == False
    assert is_valid("MH!14") == False
    assert is_valid("MH 14") == False


if __name__ == "__main__":
    main()