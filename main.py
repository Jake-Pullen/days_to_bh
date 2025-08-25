import requests
from datetime import datetime, date


def get_uk_bank_holidays():
    """Fetch bank holidays from GOV.UK API"""
    url = "https://www.gov.uk/bank-holidays.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def get_next_bank_holiday(holidays_data):
    """Find the next bank holiday after today"""
    if not holidays_data:
        return None

    today = date.today()
    next_holiday = None
    min_diff = None

    if "england-and-wales" not in holidays_data:
        return None

    for event in holidays_data["england-and-wales"]["events"]:
        try:
            holiday_date = datetime.strptime(event["date"], "%Y-%m-%d").date()

            if holiday_date < today:
                continue

            diff = (holiday_date - today).days
            if min_diff is None or diff < min_diff:
                min_diff = diff
                next_holiday = {
                    "title": event["title"],
                    "date": holiday_date,
                    "days_until": diff,
                }
        except (ValueError, KeyError):
            continue

    return next_holiday


def main():
    print("Fetching UK Bank Holidays...")

    # Get bank holidays data
    holidays_data = get_uk_bank_holidays()

    if not holidays_data:
        print("Failed to retrieve bank holiday data")
        return

    # Find next bank holiday
    next_holiday = get_next_bank_holiday(holidays_data)

    if next_holiday:
        print(f"\nNext Bank Holiday:")
        print(f"Title: {next_holiday['title']}")
        print(f"Date: {next_holiday['date'].strftime('%d/%m/%Y')}")
        print(f"Days until: {next_holiday['days_until']}")

        if next_holiday["days_until"] == 0:
            print("Today is a bank holiday! 🎉")
        elif next_holiday["days_until"] == 1:
            print("Tomorrow is a bank holiday!")
    else:
        print("No upcoming bank holidays found")


if __name__ == "__main__":
    main()
