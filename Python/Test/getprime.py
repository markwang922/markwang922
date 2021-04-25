# 题目：判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

# -*- coding: utf-8 -*-

import math


def get_prime_answer(arg):
    h = 0
    leap = 1
    from math import sqrt
    from sys import stdout
    for m in range(1, arg):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % m)
            h += 1
            if h % 10 == 0:
                print('')
        leap = 1
    print('The total is %d' % h)


def get_prime(arg):
    x = 0
    f = True
    prime = []
    for i in range(2, arg):
        # int() would just cut the front part of the float number.
        # so, we need to +1 as the divisor.
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                f = False
                break
        if f:
            # print("%d is a prime." % i)
            prime.append(i)
            x += 1

        f = True
    return prime

    print("There are total %d prime numbers." % x)


if __name__ == '__main__':
    get_prime(201)
