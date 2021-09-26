# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-26 12:54
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def dynamic_programming(a_str: str, b_str: str, insert_cost: int, delete_cost: int, replace_cost: int):
    n, m = len(a_str), len(b_str)
    dp = [[None for j in range(m + 1)] for i in range(n + 1)]

    # base case
    rows, cols = n + 1, m + 1
    for i in range(rows):
        dp[i][0] = i * delete_cost
    for j in range(cols):
        dp[0][j] = j * insert_cost

    # transfer equation
    for i in range(1, rows):
        for j in range(1, cols):
            if a_str[i - 1] == b_str[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + replace_cost
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + delete_cost, dp[i][j - 1] + insert_cost)

    return dp[rows - 1][cols - 1]


def dynamic_programming_with_space_compress(a_str: str, b_str: str, insert_cost: int, delete_cost: int,
                                            replace_cost: int):
    n, m = len(a_str), len(b_str)
    min_len = min(n, m)
    max_len = max(n, m)
    if min_len == n:  # 这里是n不是m
        insert_cost, delete_cost = delete_cost, insert_cost
        a_str, b_str = b_str, a_str
    dp = [None for i in range(min_len + 1)]

    # base case
    dp_len = min_len + 1
    for j in range(dp_len):
        dp[j] = j * insert_cost

    # transfer equation
    for i in range(1, max_len + 1):
        left_up = dp[0]
        dp[0] = i * delete_cost
        for j in range(1, dp_len):
            up = dp[j]
            if a_str[i - 1] == b_str[j - 1]:
                dp[j] = left_up
            else:
                dp[j] = left_up + replace_cost
            dp[j] = min(dp[j], up + delete_cost, dp[j - 1] + insert_cost)
            left_up = up  # 一定要注意这个left_up是还没更新的dp[j] 就是up

    return dp[dp_len - 1]


if __name__ == "__main__":
    # str1 = input()
    # str2 = input()
    # ic, dc, rc = [int(k) for k in input().split(' ')]
    str1 = 'abc'
    str2 = 'adc'
    ic, dc, rc = 5, 3, 2
    print(dynamic_programming_with_space_compress(str1, str2, ic, dc, rc))
