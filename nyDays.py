from datetime import datetime


def days2NY():
    now = datetime.today()
    NY = datetime(now.year + 1, 1, 1)
    d = NY-now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    return ('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
