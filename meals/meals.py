def main():
# getting user input
    answer = input("What time is it? ")
# Time conversion
    time = convert(answer)

# Conditions to get the result
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
# spliting the hours and minutes
    hours,minutes = time.split(":")
    new_minute = float(minutes) / 60
    return float(hours) + new_minute


if __name__ == "__main__":
    main()