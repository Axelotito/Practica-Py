import datetime, bday_messages

today = datetime.datetime.today()
next_bday = datetime.datetime(2025, 3, 30)
days_away = next_bday - today
months = int(days_away.days / 30)
other_days = days_away.days % 30

if today == next_bday:
    print(bday_messages.birthday_message())
else:
    print(f"My next bithday is {days_away.days} days away!")
    print(f"{months} months and {other_days} day away!")
