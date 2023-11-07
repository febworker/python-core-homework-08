from datetime import date, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(days=7)

    # Визначаємо день тижня
    current_weekday = today.weekday()

    # Створюємо словник для збереження імен користувачів за днями тижня
    birthdays_by_day = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Перевіряємо, чи день народження вже пройшов у поточному році, і переносимо його на наступний рік, якщо так
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження припадає на наступний тиждень
        if today <= birthday <= next_week:
            day_index = birthday.weekday()
            if day_index == 5 or day_index == 6:
                # Якщо день народження припадає на вихідний, переносимо його на понеділок
                day_index = 0
            day = list(birthdays_by_day.keys())[day_index]
            birthdays_by_day[day].append(name)

    # Перевіряємо, чи всі дні народження користувачів вже минули у цьому році
    if not any(birthdays_by_day.values()):
        return {}

    # Видаляємо дні без привітань
    birthdays_by_day = {day: names for day, names in birthdays_by_day.items() if names}

    return birthdays_by_day
