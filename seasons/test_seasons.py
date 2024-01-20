from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("2000-03-05") == ("2000","03","05")
    assert check_birthday("2002-11-22") == ("2002","11","22")
    assert check_birthday("2000-5-3") == None
    assert check_birthday("march, 5-2000") == None

if __name__ == '__main__':
    main()