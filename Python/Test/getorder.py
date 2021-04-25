# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# -*- coding: utf-t -*-

def get_order(*args):
    te = list(args)
    te.sort()
    # print(te)
    for i in te:
        print(i)


def get_order_answer():
    l = []
    for i in range(3):
        x = int(input('integer:\n'))
        l.append(x)
    l.sort()
    print(l)


if __name__ == '__main__':
    x = int(input("Please enter x: "))
    y = int(input("Please enter y: "))
    z = int(input("Please enter z: "))

    get_order(x, y, z)