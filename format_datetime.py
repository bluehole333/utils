import datetime


def format_datetime(target_time):
    """
    距离当前时间
    :param target_time: datetime
    :return: xx天前
    """
    day_date = datetime.datetime.now()
    day = (day_date - target_time).days
    minute = round((day_date - target_time).total_seconds() / 60)
    hour = round((day_date - target_time).total_seconds() / 60 / 60)

    if day:
        return '%s天前' % day
    elif 24 > hour > 0:
        return '%s小时前' % hour
    elif 60 > minute > 0:
        return '%s分钟前' % minute
    else:
        return '刚刚'
