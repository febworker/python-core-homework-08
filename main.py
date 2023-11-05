from datetime import date, timedelta
def get_birthdays_per_week(users):
    # Створюємо словник для днів тижня
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthday_dict = {day: [] for day in weekdays}
    # Отримуємо поточну дату
    today = date.today()
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        # Визначаємо, який день тижня відповідає дню народження
        day_of_week = birthday.strftime("%A")
        # Якщо день народження вже минув у цьому році, переносимо його на наступний рік
        if today > birthday:
            birthday = birthday.replace(year=today.year + 1)
            day_of_week = birthday.strftime("%A")
        # Додаємо ім'я користувача до відповідного дня тижня
        if day_of_week in birthday_dict:
            birthday_dict[day_of_week].append(name)
    # Перевіряємо, чи поточний день - вихідний (Saturday або Sunday)
    if today.weekday() == 5 or today.weekday() == 6:
        # Переносимо дні народження з вихідних на понеділок
        if birthday_dict['Saturday']:
            birthday_dict['Monday'] += birthday_dict['Saturday']
        if birthday_dict['Sunday']:
            birthday_dict['Monday'] += birthday_dict['Sunday']
        birthday_dict['Saturday'] = []
        birthday_dict['Sunday'] = []
    return birthday_dict
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date.today() + timedelta(days=2)},
        {"name": "Bill Gates", "birthday": date.today() - timedelta(days=1)},
        {"name": "Kim", "birthday": date.today() + timedelta(days=5)},
    ]
    result = get_birthdays_per_week(users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
