# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-25 15:24
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def max_points(array: List[int]):
    length = len(array)
    if length == 0:
        return 0
    array.insert(0, 1)  # 在数组两端添加1 而不去打爆它们 则可以很方便地不用考虑数组越界的情况
    array.append(1)
    return recur(array, 1, length)


def recur(array: List[int], left: int, right: int):
    if left > right:
        return 0
    temp_max_points = 0
    for i in range(left, right + 1):
        temp_max_points = max(temp_max_points,
                              array[left - 1] * array[i] * array[right + 1] + recur(array, left, i - 1) + recur(array,
                                                                                                                i + 1,
                                                                                                                right))
    return temp_max_points


def dynamic_programming(array: List[int]):
    length = len(array)
    if length == 0:
        return 0
    array.insert(0, 1)  # 在数组两端添加1 而不去打爆它们 则可以很方便地不用考虑数组越界的情况
    array.append(1)

    new_length = length + 2
    dp = [[0 for j in range(new_length)] for i in range(new_length)]

    # base case
    for i in range(1, new_length - 1):
        dp[i][i] = array[i - 1] * array[i] * array[i + 1]

    # transfer equation
    for i in range(new_length - 2, 0, -1):
        for j in range(i + 1, new_length - 1):
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + array[i - 1] * array[k] * array[j + 1] + dp[k + 1][j])  # 此时一定要将i j k的含义用递归的方式去理解 k代表的是最后一个打爆的 所以其一定不能写成array[k - 1] * array[k] * array[k + 1]

    return dp[1][new_length-2]


if __name__ == "__main__":
    # n = int(input())
    # arr = [int(k) for k in input().split()]
    n = 3
    arr = [3, 2, 5]
    print(dynamic_programming(arr))
