from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        diff = today_date - date
        return diff.days
    except ValueError:
        print("Invalid date")
