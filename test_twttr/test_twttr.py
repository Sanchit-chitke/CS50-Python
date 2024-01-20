from twttr import shorten

def main():
    test_upper_lower_case()
    test_number()
    test_punctuation()


# testing the upper and lower case
def test_upper_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TWitTeR") == "TWtTR"
# testing the number input
def test_number():
    assert shorten("1234") == "1234"

# testing the punctuation
def test_punctuation():
    assert shorten("?,.':") == "?,.':"




if __name__ == "__main__":
    main()