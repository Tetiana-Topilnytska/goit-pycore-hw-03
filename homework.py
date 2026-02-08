from datetime import datetime, timedelta
import random
import re


# Task 1
def get_days_from_today(date: str) -> int:
    """Return the day difference from today.

    Prints "Invalid date" and returns None on bad input.
    """
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.now().date()
        diff = today_date - date
        return diff.days
    except ValueError:
        print("Invalid date")


# Task 2
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Return sorted unique random numbers within bounds.

    Expects min>=1, max<=1000, and a valid quantity; otherwise returns [].
    """
    if min < 1:
        return []
    elif max > 1000:
        return []
    elif min > max:
        return []
    elif max - min <= quantity:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers


# Task 3
def normalize_phone(phone_number: str) -> str:
    """Normalize a phone number to a +38... format.

    If number already has country code 38, just add '+'; otherwise prefix '+38'.
    """
    pattern = r"\D"
    clean_phone = re.sub(pattern, "", phone_number)
    if clean_phone.startswith("38"):
        return f"+{clean_phone}"
    else:
        return f"+38{clean_phone}"


# Task 4
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Return upcoming birthdays in the next 7 days.

    Weekend birthdays are shifted to the following Monday.
    """
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


if __name__ == "__main__":
    print("Task 1")
    print(get_days_from_today("2021-10-09"))
    print()

    print("Task 2")
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
    print()

    print("Task 3")
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    print()

    print("Task 4")
    users = [
        {"name": "John Doe", "birthday": "1985.02.14"},
        {"name": "Jane Smith", "birthday": "1990.02.10"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
