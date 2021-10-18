# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-18 09:37
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
from typing import List


def get_palindrome(chars: List[str]):
    length = len(chars)
    if length <= 1:
        return ''.join(chars)

    # base case
    dp = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        dp[i][i] = 0
    # 计算如dp[0][1] dp[1][2]时 若chars[i]==chars[j] 则需要考虑dp[i+1][j-1] 即dp[1][0] dp[2][1] 而到了需要考虑这一步的时候 结果也必为0 所以直接将所有的dp[i][i-1]初始化为0
    # 一开始就已经是0 这里显式初始化则是为了强调这一点
    for i in range(1, length):
        dp[i][i - 1] = 0
    # dp[i][j]的计算依赖于其左方 下方 以及左下方的位置 因此可以得出遍历的方向
    for i in range(length - 2, -1, -1):
        for j in range(i + 1, length):
            if chars[i] == chars[j]:  # cabc的填充最小回文字符串一定是ab变成回文字符串后两边+c 而不是cab变成回文字符串后两边+c 因为后者必为cc***cc的形式而***正好为ab所变成的回文字符串 此时明显长于前者
                min_add = dp[i + 1][j - 1]
            else:
                min_add = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1)
            dp[i][j] = min_add

    # 根据dp数组的情况重建最小回文字符串
    result = ['' for i in range(dp[0][length - 1] + length)]
    left, right = 0, length - 1
    res_left, res_right = 0, len(result) - 1
    while left <= right:
        if chars[left] == chars[right]:
            result[res_left], result[res_right] = chars[left], chars[left]
            left += 1
            right -= 1
        else:
            if dp[left][right] == dp[left + 1][right] + 1:
                result[res_left], result[res_right] = chars[left], chars[left]
                left += 1
            else:
                result[res_left], result[res_right] = chars[right], chars[right]
                right -= 1
        res_left += 1
        res_right -= 1

    return ''.join(result)


if __name__ == "__main__":
    test = list(input())
    print(get_palindrome(test))
