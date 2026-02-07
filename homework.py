from datetime import datetime
import random


# Task 1
def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        diff = today_date - date
        return diff.days
    except ValueError:
        print("Invalid date")


# Task 2
def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return []
    elif max > 1000:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers
