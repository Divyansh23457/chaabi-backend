def f(date, n):
    year, month, day = map(int, date.split('-'))
    days_in_month = {
        1: 31,  
        2: 28, 
        3: 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10: 31,  
        11: 30,  
        12: 31   
    }

    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap_year:
        days_in_month[2] = 29
    while n > 0:
        day -= 1
        if day == 0:
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            day = days_in_month[month]
        n -= 1
    date_before = f"{year:02d}-{month:02d}-{day:02d}"
    return date_before


print(f('16-12-10',11))