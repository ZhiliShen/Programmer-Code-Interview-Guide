# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-26 21:29
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def dynamic_programming(array: List[int]):
    n = len(array)
    if n == 0:
        return 0
    dp = [0 for i in range(n)]
    dictionary = {0: -1}
    # base case
    if array[0] == 0:
        dp[0] = 1
    else:
        dp[0] = 0
    dictionary[array[0]] = 0

    # transfer equation
    xor_sum = array[0]
    for i in range(1, n):
        xor_sum = xor_sum ^ array[i]
        index = dictionary.get(xor_sum, None)  # 这里不能写dictionary.get(xor_sum, False) 因为False等价于0 而如果键对应的值是0 就会产生歧义
        if index is not None:
            dp[i] = dp[index] + 1 if index != -1 else 1
        else:
            dp[i] = 0
        dictionary[xor_sum] = i
        dp[i] = max(dp[i - 1], dp[i])

    return dp[n - 1]


if __name__ == "__main__":
    n = int(input())
    arr = [int(k) for k in input().split()]
    print(dynamic_programming(arr))
