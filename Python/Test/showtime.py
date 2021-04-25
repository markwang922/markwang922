# 题目：暂停一秒输出，并格式化当前时间。

# _*_ coding: utf-8 -*-

from time import localtime, sleep, strftime, time


def show_time():
    local_time = localtime(time())
    print(strftime("%Y/%m/%d %H:%M:%S", local_time))

    sleep(1)

    local_time = localtime(time())
    print(strftime("%Y %m %d %H:%M:%S", local_time))


def show_time_answer():
    print(strftime('%Y-%m-%d %H:%M:%S', localtime(time())))

    # 暂停一秒
    sleep(1)

    print(strftime('%Y-%m-%d %H:%M:%S', localtime(time())))


if __name__ == '__main__':
    show_time()
