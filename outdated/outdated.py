months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
        else:
            old_month, old_day, year = date.split(" ")
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
            day_parts = old_day.split(",")
            if len(day_parts) == 2:
                day = day_parts[0].strip()
                if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                    break
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        print()
        pass

if "/" in date or len(day_parts) == 2:
    print(f"{year}-{int(month):02}-{int(day):02}")