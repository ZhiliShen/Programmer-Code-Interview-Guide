# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-28 18:12
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def f(array: List[int], left: int, right: int):
    if left == right:
        return array[left]
    return max(array[left] + s(array, left + 1, right), array[right] + s(array, left, right - 1))  # 我方先选所获得的分数是从选择一端后所获得分数加上后选所能获得的最大分数


def s(array: List[int], left: int, right: int):
    if left == right:
        return 0
    return min(f(array, left, right - 1), f(array, left + 1, right))  # 主动权交给对方 对方选择完则会转换为我方先选 而对方必然将最坏的情况留给我方


def recur(array: List[int]):
    return max(f(array, 0, len(array) - 1), s(array, 0, len(array) - 1))


def dynamic_programming(array: List[int]):
    length = len(array)
    f_dp = [[None for j in range(length)] for i in range(length)]
    s_dp = [[None for j in range(length)] for i in range(length)]

    # base case
    for i in range(length):
        f_dp[i][i] = array[i]
    for i in range(length):
        s_dp[i][i] = 0

    # transfer equation
    for i in range(length-1, -1, -1):
        for j in range(i+1, length):
            f_dp[i][j] = max(array[i]+s_dp[i+1][j], array[j]+s_dp[i][j-1])
            s_dp[i][j] = min(f_dp[i][j-1], f_dp[i+1][j])

    return max(f_dp[0][length-1], s_dp[0][length-1])


if __name__ == "__main__":
    n = int(input())
    test = [int(k) for k in input().split()]  # 可以将一个有分隔符的数字字符串的每一位拆分出来
    print(dynamic_programming(test))
