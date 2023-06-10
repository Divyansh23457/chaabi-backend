def f(from_date, to_date, difference):

    from_year, from_month, from_day = map(int, from_date.split('-'))
    to_year, to_month, to_day = map(int, to_date.split('-'))

    from_days = from_year * 365 + from_month * 30 + from_day
    to_days = to_year * 365 + to_month * 30 + to_day

    date_difference = abs(to_days - from_days)

    if date_difference < difference:
        return True
    else:
        return False

print(f('22-02-02','22-02-05',2))