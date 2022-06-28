from datetime import datetime as dt

fmt_regex = r"\w+=(((MO|TU|WE|TH|FR|SA|SU)\d\d:\d\d-\d\d:\d\d)[,|\n]+)+"
# fmt_regex = "\\w+=(((((MO|TU|WE|TH|FR|SA|SU)(\\d\\d:\\d\\d)))-(((\\d\\d:\\d\\d))))[,|\\n]+)*"
fmt_hour = "%H:%M"

values_weekday = {
    (dt.strptime("00:01", fmt_hour), dt.strptime("09:00", fmt_hour), 25),
    (dt.strptime("09:01", fmt_hour), dt.strptime("18:00", fmt_hour), 15),
    (dt.strptime("18:01", fmt_hour), dt.strptime("23:59", fmt_hour), 20),
}
values_weekend = {
    (dt.strptime("00:01", fmt_hour), dt.strptime("09:00", fmt_hour), 30),
    (dt.strptime("09:01", fmt_hour), dt.strptime("18:00", fmt_hour), 20),
    (dt.strptime("18:01", fmt_hour), dt.strptime("23:59", fmt_hour), 25),
}
schedule = {
    'MO': values_weekday,
    'TU': values_weekday,
    'WE': values_weekday,
    'TH': values_weekday,
    'FR': values_weekday,
    'SA': values_weekend,
    'SU': values_weekend
}



