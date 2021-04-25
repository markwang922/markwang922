# 题目：斐波那契数列。

# -*- coding: utf-8 -*-


from time import sleep


def get_fibonacci():
    fibo = [0, 1]

    for i in fibo:
        print(i, end=',')
    while 1:
        nex = fibo[-1] + fibo[-2]
        fibo.append(nex)
        print(nex, end=',')
        sleep(1)


def get_fibonacci_answer():
    def fib(n):
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a

    # 输出了第10个斐波那契数列
    print(fib(10))


def get_fibonacci_answer2():
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    
if __name__ == '__main__':
    get_fibonacci()