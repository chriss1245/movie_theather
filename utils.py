import datetime
def date_to_dict(date: datetime.datetime) -> dict:
    date_dict = {
        'hour': date.hour,
        'minute': date.minute,
        'day': date.day,
        'month': date.month,
        'year': date.year,
        'weekday': date.weekday() + 1 #datetime.weekday() returns mon = 0.. sun = 6, we changed it so that the indexes at js match
    }
    return date_dict