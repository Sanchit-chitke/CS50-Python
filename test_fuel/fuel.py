def main():
     fraction = input("Fraction: ")
     fraction_converted = convert(fraction)
     output = gauge(fraction_converted)
     print(output)


def convert(fraction):
        while True:

                    try:
                        # Splitting the input into numerator and denomenator
                        numerator, denomenator = fraction.split("/")
                        # conversion of string to the int
                        x = int(numerator)
                        y = int (denomenator)

                        # doing the division of the input
                        f = x / y
                        if f <= 1:
                             p = int(round(f * 100))
                             return p
                        else:
                             fraction = input("Fraction: ")
                             pass
                    except (ValueError,ZeroDivisionError):
                         raise

def gauge(percentage):
# if the percentage is less than 1 print E
    if percentage <= 1:
        return "E"
# if the percentage is grater or equal to 99 print F
    elif percentage >= 99:
        return "F"
# otherwise print the percentage of the fuel
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()