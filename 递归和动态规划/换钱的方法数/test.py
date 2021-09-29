# -*- coding: utf-8 -*- #
# @Time    : 2021/8/19 22:37
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List


def process_1(arr: List[int], i: int, rest: int):
    res = 0
    if i == len(arr):
        if rest == 0:
            return 1
        else:
            return 0
    k = 0
    while k*arr[i] <= rest:
        res += process_1(arr, i+1, rest-k*arr[i])
        k += 1
    return res


def coins_1(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    return process_1(arr, 0, aim)


def process_2(arr: List[int], i: int, rest: int, coins_map: List[List]):
    res = 0
    if i == len(arr):
        if rest == 0:
            return 1
        else:
            return 0
    k = 0
    while k * arr[i] <= rest:
        temp = coins_map[i+1][rest - k * arr[i]]
        if temp is not None:
            res += temp
        else:
            res += process_2(arr, i + 1, rest - k * arr[i], coins_map)
        k += 1
    coins_map[i][rest] = res
    return res


def coins_2(arr: List[int], aim: int):  # Memorization Search
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    coins_map = [[None for i in range(aim+1)] for j in range(len(arr)+1)]
    return process_2(arr, 0, aim, coins_map)


def coins_3(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [[0 for i in range(aim+1)] for j in range(len(arr))]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(len(dp[0])):
        if i % arr[0] == 0:
            dp[0][i] = 1
    for i in range(1, len(dp)):
        for rest in range(1, len(dp[0])):
            k = 0
            while k * arr[i] <= rest:
                dp[i][rest] += dp[i-1][rest - k * arr[i]]
                k += 1

    return dp[i][rest]


def coins_4(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [[0 for j in range(aim+1)] for i in range(len(arr))]

    # base case
    for i in range(len(dp)):
        dp[i][0] = 1
    for j in range(len(dp[0])):
        if j % arr[0] == 0:
            dp[0][j] = 1

    # transfer equation:
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i-1][j]
            dp[i][j] += dp[i][j-arr[i]] if j-arr[i] >= 0 else 0

    return dp[len(arr)-1][aim]


def coins_5(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [0 for i in range(aim+1)]

    # base case
    for j in range(len(dp)):
        if j % arr[0] == 0:
            dp[j] = 1

    # transfer equation:
    for i in range(1, len(arr)):
        dp[0] = 1
        for j in range(1, len(dp)):
            dp[j] = (dp[j]+(dp[j-arr[i]] if j-arr[i] >= 0 else 0)) % 1000000007  # 三目运算符记得打括号！

    return dp[aim]


if __name__ == "__main__":
    n, aim = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(coins_5(arr, aim))
