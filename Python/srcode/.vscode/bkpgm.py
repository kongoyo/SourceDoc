from datetime import datetime, timedelta

start_date = datetime(2023, 5, 1)
end_date = datetime(2023, 12, 31)

exclude_dates = [datetime(2023, 5, 3), datetime(2023, 6, 12), datetime(2023, 11, 1)]

current_date = start_date
number = 1

while current_date <= end_date:
    if current_date.weekday() < 5 and current_date not in exclude_dates:
        print(current_date.isoweekday, sep=":", end="\n")
        number = (number % 10) + 1
        
    current_date += timedelta(days=1)
