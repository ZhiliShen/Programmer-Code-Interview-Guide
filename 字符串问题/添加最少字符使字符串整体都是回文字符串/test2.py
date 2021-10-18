# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-18 10:37
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
from typing import List


def get_palindrome(chars: str, palindrome: str):
    chars_length = len(chars)
    palindrome_length = len(palindrome)

    if chars_length <= 1:
        return chars

    result = ['' for i in range(chars_length - palindrome_length + chars_length)]

    c_left, c_right = 0, chars_length - 1
    p_left, p_right = 0, palindrome_length - 1
    r_left, r_right = 0, len(result) - 1

    while r_left <= r_right:  # 写成p_left <= p_right也是可以的 但是这样写更为直观
        t_left, t_right = c_left, c_right
        while chars[c_left] != palindrome[p_left]:
            c_left += 1
        while chars[c_right] != palindrome[p_right]:
            c_right -= 1
        # 此时t_left~c_left-1 c_right+1~t_right 为拼接区间段
        # AE 1 ** 1 DFG -> AEGFD 1 ** 1 DFGEA
        concat(result, r_left, r_right, chars, t_left, c_left, t_right, c_right)
        # 此时再增加最小回文子序列上的字符
        concat_size = c_left - t_left + t_right - c_right
        r_left += concat_size
        r_right -= concat_size
        result[r_left] = chars[c_left]
        result[r_right] = chars[c_right]
        r_left += 1
        r_right -= 1
        c_left += 1
        c_right -= 1
        p_left += 1
        p_right -= 1

    return ''.join(result)


def concat(result: List[str], r_left: int, r_right: int, chars: str, t_left: int, c_left: int, t_right: int,
           c_right: int):
    for i in range(t_left, c_left):
        result[r_left] = chars[i]
        result[r_right] = chars[i]
        r_left += 1
        r_right -= 1
    for i in range(t_right, c_right, -1):
        result[r_left] = chars[i]
        result[r_right] = chars[i]
        r_left += 1
        r_right -= 1


if __name__ == "__main__":
    test = input()
    target = input()
    print(get_palindrome(test, target))
