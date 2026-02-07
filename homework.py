from datetime import datetime
import random
import re


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


# Task 3
def normalize_phone(phone_number):
    pattern = r"\D"
    clean_phone = re.sub(pattern, "", phone_number)
    if clean_phone.startswith("38"):
        return f"+{clean_phone}"
    else:
        return f"+38{clean_phone}"