# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# -*- coding: utf-8 -*-


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(x):
    year = x
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def get_which_day(*args):
    year = args[0]
    month = args[1]
    day = args[-1]

    result = 0
    for i in range(0, month - 1):
        result += months[i]
    result += day

    if is_leap(year):
        result += 1

    return result


def get_which_day_answer(*args):
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    months2 = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 < month <= 12:
        res = months2[month - 1]
    else:
        print('data error')
    res += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        res += 1
    print('it is the %dth day.' % res)


if __name__ == '__main__':
    y = int(input("Please enter year: \t"))
    m = int(input("Please enter month: \t"))
    d = int(input("Please enter day: \t"))
    print("This is the %dth day." % get_which_day(y, m, d))
