# -*- coding: utf-8 -*- #
# @Time    : 2021/8/19 12:59
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List


def process(arr: List[int], i: int, rest: int):
    if i == len(arr):
        if rest == 0:
            return 0
        else:
            return -1
    k = 0
    min_case = float("inf")
    while k * arr[i] <= rest:
        temp = process(arr, i + 1, rest - k * arr[i])
        if temp != -1:
            min_case = min(min_case, k + temp)
        k += 1  # must remember increase k in while loop
    return min_case if min_case != float("inf") else -1


def min_coins_1(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    return process(arr, 0, aim)


def min_coins_2(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [[float("inf") for i in range(aim+1)] for j in range(len(arr)+1)]
    dp[-1][0] = 0
    for i in range(len(arr)-1, -1, -1):
        for rest in range(0, aim+1):
            k = 0
            while k*arr[i] <= rest:
                dp[i][rest] = min(dp[i+1][rest-k*arr[i]]+k, dp[i][rest])
                k += 1
    return dp[0][aim] if dp[0][aim] != float("inf") else -1


def min_coins_3(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [[float("inf") for i in range(aim+1)] for j in range(len(arr)+1)]
    dp[-1][0] = 0
    for i in range(len(arr)-1, -1, -1):
        for rest in range(0, aim+1):
            if rest - arr[i] >= 0:
                dp[i][rest] = min(dp[i][rest-arr[i]]+1, dp[i+1][rest])
            else:
                k = 0
                while k * arr[i] < rest:
                    dp[i][rest] = min(dp[i + 1][rest - k * arr[i]] + k, dp[i][rest])
                    k += 1
    return dp[0][aim] if dp[0][aim] != float("inf") else -1


def min_coins_4(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [[float("inf") for i in range(aim+1)] for j in range(len(arr)+1)]
    dp[-1][0] = 0
    for i in range(len(arr)-1, -1, -1):
        for rest in range(0, aim+1):
            if rest - arr[i] >= 0:
                dp[i][rest] = min(dp[i][rest-arr[i]]+1, dp[i+1][rest])
            else:
                dp[i][rest] = dp[i + 1][rest]
    return dp[0][aim] if dp[0][aim] != float("inf") else -1


def min_coins_5(arr: List[int], aim: int):
    if arr is None or len(arr) == 0 or aim < 1:
        return 0
    dp = [float("inf") for i in range(aim+1)]
    dp[0] = 0
    for i in range(len(arr)-1, -1, -1):
        for rest in range(0, aim+1):
            if rest - arr[i] >= 0:
                dp[rest] = min(dp[rest-arr[i]]+1, dp[rest])
    return dp[aim] if dp[aim] != float("inf") else -1


if __name__ == "__main__":
    n, aim = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(min_coins_5(arr, aim))
