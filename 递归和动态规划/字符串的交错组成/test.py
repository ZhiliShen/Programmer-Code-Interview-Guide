# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-29 17:50
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def dynamic_programming(a_str: str, b_str: str, c_str: str):
    length_a, length_b, length_c = len(a_str), len(b_str), len(c_str)
    if length_c != (length_a + length_b):
        return 'NO'
    dp = [[False for j in range(length_b + 1)] for i in range(length_a + 1)]

    # base case
    dp[0][0] = True
    for i in range(1, length_a + 1):
        if c_str[i - 1] == a_str[i - 1]:
            dp[i][0] = True
        else:
            break
    for j in range(1, length_b + 1):
        if c_str[j - 1] == b_str[j - 1]:
            dp[0][j] = True
        else:
            break

    # transfer equation:
    for i in range(1, length_a + 1):
        for j in range(1, length_b + 1):
            if dp[i - 1][j] and a_str[i - 1] == c_str[i + j - 1]:
                dp[i][j] = True
            elif dp[i][j - 1] and b_str[j - 1] == c_str[i + j - 1]:
                dp[i][j] = True
            else:
                dp[i][j] = False

    return 'YES' if dp[length_a][length_b] else 'NO'


def dynamic_programming_with_space_compress(a_str: str, b_str: str, c_str: str):
    length_a, length_b, length_c = len(a_str), len(b_str), len(c_str)
    if length_c != (length_a + length_b):
        return 'NO'
    min_length = min(length_a, length_b)
    max_length = max(length_a, length_b)
    if min_length == length_a:
        a_str, b_str = b_str, a_str
    dp = [False for i in range(min_length + 1)]

    # base case
    dp[0] = True  # !!!
    for i in range(1, min_length + 1):
        if b_str[i - 1] == c_str[i - 1]:
            dp[i] = True
        else:
            break

    # transfer equation
    for i in range(1, max_length + 1):
        if a_str[i - 1] == c_str[i - 1] and dp[0]:
            dp[0] = True
        else:
            dp[0] = False
        for j in range(1, min_length + 1):
            if dp[j] and a_str[i - 1] == c_str[i + j - 1]:
                dp[j] = True
            elif dp[j - 1] and b_str[j - 1] == c_str[i + j - 1]:
                dp[j] = True
            else:
                dp[j] = False

    return 'YES' if dp[min_length] else 'NO'


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    str3 = input()
    print(dynamic_programming_with_space_compress(str1, str2, str3))
