months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)

        elif "," in date:
            parts = date.split()
            month_name = parts[0]
            day = int(parts[1].rstrip(","))
            year = int(parts[2])
            month = months.index(month_name) + 1

        else:
            continue

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        continue
