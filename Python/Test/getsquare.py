# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？


# -*- coding: utf-8 -*-

from math import sqrt


def get_square_root():
    x = 1
    # print(x)
    while x:
        # print(sqrt(x + 100))
        if float.is_integer(sqrt(x + 100)):
            if float.is_integer(sqrt(x + 268)):
                print(x)
                # break
        x += 1


def get_square_root_answer():
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                y = m * m - 268
                print(int(x))


if __name__ == '__main__':
    print("Mark's answer is:")
    # get_square_root()

    print("The right answer is:")
    get_square_root_answer()
