# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Not using generator to get the double numbers.
from pip._vendor.urllib3.connectionpool import xrange


def double_numbers(iterable):
    double_agr = []

    for i in iterable:
        double_agr.append(i + i)

    return double_agr


# Using generator to get the double numbers.
def double_numbers_generator(iterable):
    for i in iterable:
        yield i + i


if __name__ == '__main__':
    # for value in double_numbers(range(10000)):  # `test_non_generator`
    for value in double_numbers_generator(xrange(10000)):
        print(value)
        if value > 5:
            break
