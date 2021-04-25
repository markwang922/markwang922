# 题目：将一个列表的数据复制到另一个列表中。

# -*- coding: utf-8 -*-


def copy_list(arg):
    list_in = []
    for i in arg:
        list_in.append(i)
    return list_in


if __name__ == '__main__':
    list1 = [1, 2, 4, 5, 3]
    list2 = copy_list(list1)
    print(list2)