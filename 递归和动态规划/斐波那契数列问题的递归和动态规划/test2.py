# -*- coding: utf-8 -*- #
# @Time    : 2021/8/18 7:59
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
import sys

def f1(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, n - 2)
    return 2 * res[0][0] + res[1][0]


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
    print(f1(n) % 1000000007)
