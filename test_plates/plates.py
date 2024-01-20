def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_length = len(s)
    if plate_length >= 2 and plate_length <= 6 and s[:2].isalpha() and s.isalnum():
        for i in s:
            if i.isdigit():
                number_index = s.index(i)
                if s[number_index:].isdigit() and i != str(0):
                    return True
                else:
                    return False

        return True
    else:
        return False

    
if __name__ == '__main__':
    main()