from datetime import datetime, date, timedelta, MINYEAR
import calendar

def group_birthdays_by_day(users):
    today = datetime.today()
    next_7_days = [today + timedelta(days=i) for i in range(7)]

    birthdays_next_week = {}
    
    for user in users:
        for upcoming_day in next_7_days:
            if user['birthday'].month == upcoming_day.month and user['birthday'].day == upcoming_day.day:
                day_of_week = calendar.day_name[upcoming_day.weekday()]
                if day_of_week in birthdays_next_week:
                    birthdays_next_week[day_of_week].append(user['name'])
                else:
                    birthdays_next_week[day_of_week] = [user['name']]

    if 'Saturday' in birthdays_next_week:
        if 'Monday' in birthdays_next_week:
            birthdays_next_week['Monday'].extend(birthdays_next_week['Saturday'])
        else:
            birthdays_next_week['Monday'] = birthdays_next_week['Saturday']
        del birthdays_next_week['Saturday']

    if 'Sunday' in birthdays_next_week:
        if 'Monday' in birthdays_next_week:
            birthdays_next_week['Monday'].extend(birthdays_next_week['Sunday'])
        else:
            birthdays_next_week['Monday'] = birthdays_next_week['Sunday']
        del birthdays_next_week['Sunday']

    return birthdays_next_week

birthdays_next_week = group_birthdays_by_day(users)

for day, names in birthdays_next_week.items():
    print(f"{day}: {', '.join(names)}")