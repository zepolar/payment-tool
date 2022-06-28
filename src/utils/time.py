from datetime import datetime as dt

from exception.file_exception import TimeError
from utils.constants import fmt_hour


def converter_time(time_string):
    try:
        return dt.strptime(time_string, fmt_hour)
    except ValueError:
        raise TimeError("Time data does not match format Hour:Minute")
