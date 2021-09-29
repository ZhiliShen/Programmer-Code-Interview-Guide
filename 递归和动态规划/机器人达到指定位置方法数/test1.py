# -*- coding: utf-8 -*- #
# @Time    : 2021/8/18 22:15
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
import sys
from array import array


def walk(n: int, cur: int, rest: int, p: int):
    if rest == 0:
        return 1 if cur == p else 0
    if cur == 1:
        return walk(n, 2, rest - 1, p)
    if cur == n:
        return walk(n, n - 1, rest - 1, p)
    return walk(n, cur - 1, rest - 1, p) + walk(n, cur + 1, rest - 1, p)


def ways1(n: int, m: int, k: int, p: int):
    if n < 2 or m < 1 or m > n or p < 1 or p > n or k < 1:
        return 0
    return walk(n, m, k, p)


def ways2(n: int, m: int, k: int, p: int):
    if n < 2 or m < 1 or m > n or p < 1 or p > n or k < 1:
        return 0
    dp = [[0 for j in range(n + 1)] for i in range(k + 1)]
    dp[0][p] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][2]
            elif j == n:
                dp[i][j] = dp[i - 1][n - 1]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000007
    return dp[k][m]


def ways3(n: int, m: int, k: int, p: int):
    if n < 2 or m < 1 or m > n or p < 1 or p > n or k < 1:
        return 0
    dp = array("i", [0 for i in range(n + 1)])
    dp[p] = 1
    for i in range(1, k + 1):
        up_left = dp[1]
        for j in range(1, n + 1):
            if j == 1:
                dp[j] = dp[2]
            elif j == n:
                dp[j] = up_left
            else:
                temp = dp[j]
                dp[j] = (up_left + dp[j + 1]) % 1000000007
                up_left = temp
    return dp[m]


if __name__ == "__main__":
    n, m, k, p = [int(k) for k in sys.stdin.readline().split(" ")]
    print(ways3(n, m, k, p))
