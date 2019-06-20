DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
               'Sep', 'Oct', 'Nov', 'Dec']

n = int(input('Enter an year: '))
for year in range(n, n + 1):
    is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    print(10 * '=', year, 10 * '=')
    for month in range(12):
        days = DAYS_IN_MONTH[month]
        if month == 1 and is_leap:
            days += 1
        print(MONTH_NAMES[month], 'has', days, 'days.')
