# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# -*- coding: utf-8 -*-

from math import sqrt, pow


def get_narcissus():
    for i in range(100, 1000):
        num_hundred = int(i / 100)
        # num_ten = int((i - num_hundred * 100) / 10)
        # second way to get the 'ten' number
        # num_ten = int(i / 10) % 10
        # third way to get the 'ten' number
        num_ten = i // 10 % 10
        num_one = int(i % 10)

        num_hundred = pow(num_hundred, 3)
        num_ten = pow(num_ten, 3)
        num_one = pow(num_one, 3)

        if i == (num_one + num_ten + num_hundred):
            print("%d is a narcissus number." % i)


def get_narcissus_answer():
    for n in range(100, 1000):
        i = n // 100
        j = n // 10 % 10
        k = n % 10
        if n == i * i * i + j * j * j + k * k * k:
            print(n)


if __name__ == '__main__':
    get_narcissus()
