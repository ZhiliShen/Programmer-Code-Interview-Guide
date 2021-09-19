# -*- coding: utf-8 -*- #
# @Time    : 2021/9/14 21:52
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys


def dp(string: str):
    n = len(string)
    dp_arrays = [[None for j in range(n)] for i in range(n)]
    result = 0

    # base case
    for i in range(n):
        dp_arrays[i][i] = True
        result = 1

    for i in range(n - 1):
        if string[i] == string[i + 1]:
            dp_arrays[i][i + 1] = True
            result = 2

    # transfer equation
    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            if dp_arrays[i + 1][j - 1] and string[i] == string[j]:
                dp_arrays[i][j] = True
                result = max(result, j - i + 1)
            else:
                dp_arrays[i][j] = False

    return result


def manacher(string: str):
    string = '#' + '#'.join(list(string)) + '#'
    n = len(string)
    arm_lengths = [None for i in range(n)]
    longest_right_arm = -1
    central_index = -1
    max_arm_length = 0
    for i in range(n):
        if i <= longest_right_arm:
            arm_lengths[i] = min(arm_lengths[2*central_index - i], longest_right_arm-i)
        else:
            arm_lengths[i] = 0
        while 0 <= i - arm_lengths[i] - 1 and i + arm_lengths[i] + 1 <= n - 1:
            if string[i - arm_lengths[i] - 1] == string[i + arm_lengths[i] + 1]:
                arm_lengths[i] += 1
            else:
                break
        if i + arm_lengths[i] > longest_right_arm:
            central_index = i
            longest_right_arm = i + arm_lengths[i]
        if max_arm_length < arm_lengths[i]:
            max_arm_length = arm_lengths[i]
    return max_arm_length


if __name__ == "__main__":
    s = input()
    print(manacher(s))
