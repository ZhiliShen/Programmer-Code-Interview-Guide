# -*- coding: utf-8 -*- #
# @Time    : 2021/8/19 12:11
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List


def min_path_sum1(m: List[List[int]]):
    dp = [[0 for i in range(len(m[0]))] for j in range(len(m))]
    dp[0][0] = m[0][0]
    for i in range(1, len(m[0])):
        dp[0][i] = m[0][i] + dp[0][i - 1]
    for i in range(1, len(m)):
        dp[i][0] = m[i][0] + dp[i - 1][0]
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]
    return dp[len(m)-1][len(m[0])-1]


def min_path_sum2(m: List[List[int]]):
    more = max(len(m), len(m[0]))
    less = min(len(m), len(m[0]))
    dp = [0 for i in range(less)]
    dp[0] = m[0][0]
    row_more = (more == len(m))
    for i in range(1, len(dp)):
        dp[i] = (m[0][i] if row_more else m[i][0]) + dp[i-1]  # ternary operator must be bracketed
    for i in range(1, more):
        for j in range(less):
            if j == 0:  # this is j not i
                dp[0] = dp[0] + (m[i][0] if row_more else m[0][i])  # don't forget to use add dp[0]
            else:
                dp[j] = min(dp[j-1], dp[j]) + (m[i][j] if row_more else m[j][i])
    return dp[-1]


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    print(min_path_sum2(arr))
