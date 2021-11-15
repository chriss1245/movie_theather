import datetime
def date_to_dict(date: datetime.datetime) -> dict:
    date_dict = {
        'hour': date.hour,
        'minute': date.minute,
        'day': date.day,
        'month': date.month,
        'year': date.year,
        'weekday': date.weekday() #datetime.weekday() returns mon = 0.. sun = 6
    }
    return date_dict