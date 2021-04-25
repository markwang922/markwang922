# 题目：输出 9*9 乘法口诀表。

# -*- coding: utf-8 -*-


# show the multiplication formula table
def show_multiplication():
    for x in range(1, 10):
        for y in range(1, x + 1):
            res = int(x * y)
            print('%sx%s = %d\t' % (x, y, res), end=' ')
        print()


def show_multiplication_answer():
    for i in range(1, 10):
        print()
        for j in range(1, i + 1):
            print("%d*%d=%d" % (i, j, i * j), end=" ")


if __name__ == '__main__':
    show_multiplication()
