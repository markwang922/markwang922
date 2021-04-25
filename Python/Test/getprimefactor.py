# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# -*- coding: utf-8 -*-

from getprime import get_prime
from getfactor import get_factor


def get_prime_factor_answer(n):
    print('{} = '.format(n), end=" ")
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index  # n 等于 n//index
                if n == 1:
                    print(index)
                else:  # index 一定是素数
                    print('{} *'.format(index), end=" ")
                break


def get_prime_factor(x):
    print("Show the prime of %d" % x)
    x_prime = get_prime(x)
    print(x_prime)

    print("Show the factor of %d" % x)
    x_factor = get_factor(x)
    print(x_factor)

    x_same = []
    for i in x_prime:
        for j in x_factor:
            if i == j:
                x_same.append(i)
    print(x_same)

    print("{} = ".format(x), end=' ')
    for m in x_same:
        if x == m:
            print("{}".format(x))
        elif x % m == 0:
            print("{} *".format(m), end=' ')
    print("{}".format(5))


if __name__ == '__main__':
    get_prime_factor(100)
