# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

hits = 0
dayofweek = 0 # monday
day = 0 # 1st
month = 0 # jan
year = 1900

def leapyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

while year <= 2000:
    if dayofweek == 6 and day == 0 and year > 1900:
        hits += 1
        print month, year
    dayofweek = (dayofweek + 1) % 7
    if month == 1 and leapyear(year):
        day = (day + 1) % 29
    else:
        day = (day + 1) % daysinmonth[month]
    if day == 0:
        month = (month + 1) % 12
        if month == 0:
            year = year + 1

print hits

