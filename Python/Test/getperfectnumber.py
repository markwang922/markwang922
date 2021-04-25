# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# -*- coding: utf-8 -*-

from getfactor import get_factor
from functools import reduce


def get_perfect_number():
    for i in range(1, 1001):
        # print(i)
        i_factor = get_factor(i)
        # print(i_factor)

        res = reduce(lambda x, y: x + y, i_factor, 0)

        if i == res:
            print("Perfect number is: %d" % i)


def get_perfect_number_answer():
    from sys import stdout
    for j in range(2, 1001):
        k = []
        n = -1
        s = j
        for i in range(1, j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)

        if s == 0:
            print(j)
            for i in range(n):
                stdout.write(str(k[i]))
                stdout.write(' ')
            print(k[n])


if __name__ == '__main__':
    get_perfect_number()
