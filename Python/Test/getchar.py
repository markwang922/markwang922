# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# -*- coding: utf-8 -*-

import string


def get_char(arg):
    chars_list = []

    num_int = 0
    num_str = 0
    num_spa = 0
    num_oth = 0

    for c in arg:
        chars_list.append(c)

        try:
            int(c)
        except ValueError:
            if c.isalpha():
                num_str += 1
            elif c.isspace():
                num_spa += 1
            else:
                num_oth += 1
        else:
            num_int += 1

    print("Int: %d, String: %d, space: %d, Others: %d" % (num_int, num_str, num_spa, num_oth))


def get_char_answer(arg):
    # s = input('请输入一个字符串:\n')
    letters = 0
    space = 0
    digit = 0
    others = 0
    for c in arg:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))


if __name__ == '__main__':
    str_int = input("Please enter the characters, separated with comma(,): ")
    get_char(str_int)
