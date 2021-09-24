# -*- coding: utf-8 -*- #
# @Time    : 2021-09-24 13:35
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def dynamic_programming(a_str: str, b_str: str):
    n, m = len(a_str), len(b_str)
    if len(a_str) == 0 or len(b_str) == 0:
        return 0
    dp = [[0 for j in range(m)] for i in range(n)]

    # base case
    for i in range(n):
        if a_str[i] == b_str[0]:
            while i < n:
                dp[i][0] = 1
                i += 1
            break

    for j in range(m):
        if a_str[0] == b_str[j]:
            while j < m:
                dp[0][j] = 1
                j += 1
            break

    # transfer equation
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if a_str[i] == b_str[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1]+1)

    return gen_lcs(dp, a_str, b_str) if dp[i][j] != 0 else -1


def gen_lcs(dp: List[List[int]], a_str: str, b_str: str):
    n, m = len(dp), len(dp[0])
    i, j = n - 1, m - 1
    index = dp[i][j] - 1
    res = [None for i in range(dp[i][j])]

    while index >= 0:  # 需要考虑index等于1时 此时i和j中的某一个已经等于0了 是没有办法和左上角的数字进行比较的 所以这个时候直接取相应的字符即可
        if j > 0 and dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            res[index] = a_str[i]
            i -= 1
            j -= 1
            index -= 1

    return "".join([str(i) for i in res])


def dynamic_programming_with_space_compress(a_str: str, b_str: str):
    n, m = len(a_str), len(b_str)
    if len(a_str) == 0 or len(b_str) == 0:
        return 0

    if n > m:  # 假设a_str是较短的那一个
        n, m = m, n
        a_str, b_str = b_str, a_str

    dp = [0 for i in range(n)]

    # base case
    for i in range(n):
        if a_str[i] == b_str[0]:
            while i < n:
                dp[i] = 1
                i += 1
            break

    # transfer equation
    for j in range(1, m):
        prev_left_up = dp[0]  # prev_left_up代表左上角的值
        dp[0] = max(dp[0], 1 if b_str[j] == a_str[0] else 0)
        for i in range(1, n):
            cur_left_up = dp[i]  # 需要存下当前的值 但是还不能替换prev_left_up 因为prev_left_up还没用
            dp[i] = max(dp[i-1], dp[i])
            if a_str[i] == b_str[j]:
                dp[i] = max(prev_left_up+1, dp[i])
            prev_left_up = cur_left_up  # prev_left_up用完了要更新

    return dp[-1]



if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(dynamic_programming(str1, str2))
