NUM_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK_DAY_NAMES = ['Четвъртък', 'Петък', 'Събота', 'Неделя',
                  'Понеделник', 'Вторник', 'Сряда']

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def calc_num_days_in_month(year, month):
    n = NUM_DAYS[month - 1]
    if month == 2 and is_leap_year(year):
        return n + 1
    return n


def is_valid_date(date):
    """Takes a list of 3 numbers, returns if it is a valid date."""
    
    year, month, day = date
    assert type(year) == type(month) == type(day) == int
    if not 1 <= month <= 12:
        return False
    if day < 1 or day > calc_num_days_in_month(year, month):
        return False
    return True


def enter_date():
    while True:
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        date = [year, month, day]
        if is_valid_date(date):
            break
        print('This is not a valid date. Please try again.')
    return date


def calc_next_date(date):
    assert is_valid_date(date)
    year, month, day = date
    if day == calc_num_days_in_month(year, month):
        next_day = 1
        next_month = month + 1
    else:
        next_day = day + 1
        next_month = month
    if next_month == 13:
        next_month = 1
        next_year = year + 1
    else:
        next_year = year
    return [next_year, next_month, next_day]


def calc_days_interval(date1, date2):
    """Returns the number of days between date1 and date2.

    date1 and date2 must be lists of 3 integers [year, month, day].
    """
    
    if date1 > date2:
        return - calc_days_interval(date2, date1)
    day_count = 0
    while date1 < date2:
        date1 = calc_next_date(date1)
        day_count += 1
    return day_count
    
def calc_day_of_week(date):
    assert is_valid_date(date)
    n = calc_days_interval([2019, 2, 21], date)
    return WEEK_DAY_NAMES[n % 7]


date = enter_date()
day_of_week = calc_day_of_week(date)
print(day_of_week)


# http://introtopython.org/introducing_functions.html
# date: [year, month, day]
#
# is_leap_year(year) -> bool
# calc_num_days_in_month(year, month) -> int
# is_valid_date(date) -> bool
# enter_date() -> date
# calc_next_date(date) -> date
# calc_days_interval(date1, date2) -> int
# calc_day_of_week(date) -> str
