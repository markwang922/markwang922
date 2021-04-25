# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import time

# def get_res():
#     from functools import reduce
#
#     Tn = 0
#     Sn = []
#     n = int(input('n = '))
#     a = int(input('a = '))
#     for count in range(n):
#         Tn = Tn + a
#         a = a * 10
#         Sn.append(Tn)
#         print(Tn)
#
#     Sn = reduce(lambda x, y: x + y, Sn)
#     print("计算和为：", Sn)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 0:
        a = input("please enter a: ")
        acc = int(input("please enter l: "))

        res = 0
        for i in range(1, acc + 1):
            res += int(a * i)
        print(res)

    from functools import reduce

    result = reduce(lambda x, y: x + y, range(1, 101))
    print(result)
