# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-30 11:05
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
from typing import List


def hanoi_state(arr: List[int], index: int, source: int, target: int, auxiliary: int):
    if index == -1:
        return 0
    if arr[index] == auxiliary:
        return -1
    if arr[index] == source:
        return hanoi_state(arr, index - 1, source, auxiliary, target)
    else:
        rest = hanoi_state(arr, index - 1, auxiliary, target, source)
        if rest == -1:
            return -1
        else:
            return 1 << index + rest  # 1<<i == 2^i


def hanoi_state_without_recur(arr: List[int], source: int, target: int, auxiliary: int):
    if arr is None or len(arr) == 0:
        return -1
    result = 0
    index = len(arr)-1
    dp = [0]*len(arr)
    last = 1
    for i in range(len(dp)):
        dp[i] = last
        last = (last << 1) % 1000000007  # 提前打表
    while index >= 0:
        if arr[index] == auxiliary:
            return -1
        if arr[index] == target:
            result += dp[index]  # 这里是index不是i！！！
            source, auxiliary = auxiliary, source
        else:
            target, auxiliary = auxiliary, target
        index -= 1

    return result % 1000000007


if __name__ == "__main__":
    n = int(input())
    test = [int(k) for k in input().split()]
    print(hanoi_state_without_recur(test, 1, 3, 2))
