def format_date(day, month, year):
    return f"{day}/{month}/{year}"

date = [15, 3, 1974]
print(date)
print(format_date(*date))