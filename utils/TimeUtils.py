import calendar
import datetime


def floattime_to_datatime(t: float) -> datetime.datetime:
    return datetime.datetime.utcfromtimestamp(t)


# https://stackoverflow.com/questions/54935647/opposite-function-to-utcfromtimestamp
def datatime_to_floattime(t: datetime.datetime) -> float:
    utc_tuple = t.utctimetuple()
    return calendar.timegm(utc_tuple)
