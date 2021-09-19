# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-19 17:11
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
import sys


def manacher(string: str):
    string = '#' + '#'.join(list(string)) + '#'
    n = len(string)
    arm_lengths = [None for i in range(n)]
    longest_right_arm = -1
    central_index = -1
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
        if longest_right_arm == n-1:
            break

    start = 2*central_index-(n-1)-1
    add_string = string[start:0:-2]

    return add_string


if __name__ == "__main__":
    s = input()
    print(manacher(s))
