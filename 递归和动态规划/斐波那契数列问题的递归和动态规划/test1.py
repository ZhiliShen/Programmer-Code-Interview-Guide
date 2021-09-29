# -*- coding: utf-8 -*- #
# @Time    : 2021/8/18 6:09
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
import sys


def f1(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return f1(n - 1) + f1(n - 2)


def f2(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    pre = 1
    pre_pre = 1
    res = 0
    for i in range(3, n + 1):
        res = pre + pre_pre
        pre_pre = pre
        pre = res
    return res


def f3(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, n - 2)
    return res[0][0] + res[1][0]


def matrix_power(base, p: int):
    res = [[0 for i in range(len(base[0]))] for j in range(len(base))]  # res must be identity matrix!
    for i in range(len(res)):
        res[i][i] = 1
    temp = base
    while p != 0:
        if p & 1 != 0:
            res = multi_matrix(res, temp)
        temp = multi_matrix(temp, temp)
        p >>= 1
    return res


def multi_matrix(a, b):
    res = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % 1000000007
    return res


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(f3(n) % 1000000007)
