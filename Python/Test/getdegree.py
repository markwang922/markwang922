# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# -*- coding: utf-8 -*-

def get_degree(arg):
    if arg >= 90:
        print("You would get degree: %s" % 'A')
    elif arg >= 60:
        print("You would get degree: %s" % 'B')
    else:
        print("You would get degree: %s" % 'C')


if __name__ == '__main__':
    while 1:
        sco = int(input("Please enter you score: "))
        get_degree(sco)