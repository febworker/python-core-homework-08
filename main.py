from datetime import date, timedelta
def get_birthdays_per_week(users):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthday_dict = {day: [] for day in weekdays}
    today = date.today()
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        day_of_week = birthday.strftime("%A")
        if today > birthday:
            birthday = birthday.replace(year=today.year + 1)
            day_of_week = birthday.strftime("%A")
        if day_of_week in birthday_dict:
            birthday_dict[day_of_week].append(name)
    if today.weekday() == 5 or today.weekday() == 6:
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
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
