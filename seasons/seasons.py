import re
import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    try:
        year , month ,day = check_birthday(birthday)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(int(year), int(month), int(day))
    today_date = date.today()
    diff = today_date - date_of_birth
    total_min = diff.days * 24 * 60
    output = p.number_to_words(total_min , andword="")
    print(output.capitalize() + " minutes")


def check_birthday(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day


if __name__ == "__main__":
    main()