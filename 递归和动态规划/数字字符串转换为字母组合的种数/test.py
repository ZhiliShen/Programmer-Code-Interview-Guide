# -*- coding: utf-8 -*- #
# @Time    : 2021-09-21 18:54
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def dynamic_programming(array: List[int]):
    if len(array) == 0:
        return 0
    length = len(array)
    # base case
    dp = [0 for i in range(length + 1)]
    dp[0] = 1  # 注意为0的时候的base case
    if 1 <= array[0] <= 9:
        dp[1] = 1
    else:
        return 0

    # transfer equation
    for i in range(2, length + 1):
        if 1 <= array[i-1] <= 9:
            if check_legal(array[i-2:i]):
                dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
            else:
                dp[i] = dp[i - 1]
        else:
            if not check_legal(array[i-2:i]):
                return 0

    return dp[-1]


def dynamic_programming_compress_space(array: List[int]):
    if len(array) == 0:
        return 0
    length = len(array)
    # base case
    prev = 1  # 注意为0的时候的base case
    if 1 <= array[0] <= 9:
        cur = 1
    else:
        return 0

    # transfer equation
    for i in range(2, length + 1):
        if 1 <= array[i-1] <= 9:
            if check_legal(array[i-2:i]):
                next = (cur + prev) % 1000000007
            else:
                next = cur
        else:
            if not check_legal(array[i-2:i]):
                return 0
        prev = cur
        cur = next

    return next


def check_legal(array: List[int]):
    if 1 <= array[0] * 10 + array[-1] <= 26:
        return True
    else:
        return False


if __name__ == "__main__":
    test = [int(k) for k in input()]
    print(dynamic_programming_compress_space(test))
