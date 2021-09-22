# -*- coding: utf-8 -*- #
# @Time    : 2021/9/22 22:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def dynamic_programming(a_str, b_str):
    n, m = len(a_str), len(b_str)
    if n == 0 or m == 0:
        return 0
    dp = [[0 for j in range(m)] for i in range(n)]
    max_len = 0
    max_index = None

    # base case
    for index, a_char in enumerate(a_str):
        if a_char == b_str[0]:
            dp[index][0] = 1
            max_len = 1
            max_index = index

    for index, b_char in enumerate(b_str):
        if b_char == a_str[0]:
            dp[0][index] = 1
            max_len = 1
            max_index = index

    # transfer equation
    for i in range(1, n):
        for j in range(1, m):
            if a_str[i] == b_str[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
                max_index = i

    return -1 if max_len == 0 else a_str[max_index+1-max_len:max_index+1]



def dynamic_programming_with_space_compress(a_str, b_str):
    n, m = len(a_str), len(b_str)
    if n == 0 or m == 0:
        return 0

    max_len = 0
    max_index = None

    row, col = 0, m-1

    while row < n:  # 循环终止的时候是要从最左下角的对角线的开头开始遍历 此时row==n-1
        i, j, temp = row, col, 0
        while i < n and j < m:  # 对角线上遍历的要求是两者都不能越界
            if a_str[i] == b_str[j]:
                temp += 1
            else:
                temp = 0
            if temp > max_len:
                max_len = temp
                max_index = i
            i += 1  # while循环记得写自增
            j += 1
        if col > 0:  # 当跳出while循环 说明该条对角线已经走到 如果列回退没有回退到第一行 则说明仍然是(0, col)模式
            col -= 1
        else:  # 当跳出while循环 且列已经没法回退 则说明是(row, 0)模式
            row += 1

    return -1 if max_len == 0 else a_str[max_index + 1 - max_len:max_index + 1]



if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(dynamic_programming_with_space_compress(str1, str2))
