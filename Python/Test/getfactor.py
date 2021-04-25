# -*- coding: utf-8 -*-

# from math import sqrt


def get_factor(arg):
    factor = []

    for i in range(1, arg):
        if arg % i == 0:
            factor.append(i)
    return factor


if __name__ == '__main__':
    print(get_factor(90))
