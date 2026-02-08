from datetime import datetime, timedelta
import random
import re


# Task 1
def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.now().date()
        diff = today_date - date
        return diff.days
    except ValueError:
        print("Invalid date")


# Task 2
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1:
        return []
    elif max > 1000:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers


# Task 3
def normalize_phone(phone_number: str) -> str:
    pattern = r"\D"
    clean_phone = re.sub(pattern, "", phone_number)
    if clean_phone.startswith("38"):
        return f"+{clean_phone}"
    else:
        return f"+38{clean_phone}"


# Task 4
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    to_congradulate = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        upcoming = birthday.replace(year=today.year)
        diff = (upcoming - today).days
        if 0 <= diff <= 7:
            if upcoming.isoweekday() in (6, 7):
                if upcoming.isoweekday() == 6:
                    congratulation_date = upcoming + timedelta(days=2)
                elif upcoming.isoweekday() == 7:
                    congratulation_date = upcoming + timedelta(days=1)

                to_congradulate.append(
                    {
                        "name": user["name"],
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                    }
                )
            else:
                to_congradulate.append(
                    {
                        "name": user["name"],
                        "congratulation_date": upcoming.strftime("%Y.%m.%d"),
                    }
                )

    return to_congradulate
