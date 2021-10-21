# -*- coding: utf-8 -*- #
# @Time    : 2021-10-21 16:14
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def min_cut(chars: str):
    chars_len = len(chars)
    if chars_len <= 1 or len(set(chars)) == 1:  # 后面len(set(chars))是为了过测试用例
        return 0
    dp_1 = [float('inf') for i in range(chars_len+1)]  # dp_1[i]表示使得[i, len-1]分割为回文子串的最小分割数
    dp_2 = [[False for j in range(chars_len)] for i in range(chars_len)]  # dp_2[i][j]表示使得[i, j]区间段是否为回文

    # base case
    dp_1[-1] = -1  # 在判断首尾时 需要借助dp[chars_len]的值 所以可以推的这里应该取-1
    dp_1[-2] = 0  # [len-1, len-1]分割为回文子串的最小分割数明显为0

    for i in range(chars_len - 2, -1, -1):
        for j in range(i, chars_len):
            if chars[i] == chars[j] and (j - i <= 1 or dp_2[i + 1][j - 1]):
                dp_1[i] = min(dp_1[i], dp_1[j + 1] + 1)
                dp_2[i][j] = True  # 单个字符必定为回文 两个字符相等也必定为回文 chars[i+1,j-1]为回文且chars[i]==chars[j] 则chars[i,j]也为回文

    return dp_1[0]  # dp_1[0]表示使得[0, len-1]分割为回文子串的最小分割数 也就是题目要求


if __name__ == "__main__":
    test = input()
    print(min_cut(test))
