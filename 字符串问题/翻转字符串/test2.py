# -*- coding: utf-8 -*- #
# @Time    : 2021-10-13 21:07
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
from typing import List


def rotate_word_1(string: List[str], size: int):
    length = len(string)
    if length == 0:
        return

    # reverse(string, 0, length - 1)
    # reverse(string, 0, length-1-size+1-1)
    # reverse(string, length-1-size+1, length - 1)

    reverse(string, 0, size - 1)
    reverse(string, size, length - 1)
    reverse(string, 0, length - 1)

    return ''.join(string)


def rotate_word_2(string: List[str], size: int):
    length = len(string)
    if length == 0:
        return

    left, right = 0, length - 1
    left_part, right_part = size, length - size
    d = left_part - right_part
    min_part = min(left_part, right_part)
    while True:
        rotate(string, left, right, min_part)
        if d == 0:
            break
        elif d > 0:  # 说明left_part > right_part 此时right_part置换到位 关注字符串后半部分
            left += min_part  # left一定是在原来的基础上递增 不能直接赋值
            left_part = d  # 因为原来的left_part有一部分直接被right_part占据了 所以新的left_part直接取d即可 而right_part仍然是不变的
        else:
            right -= min_part
            right_part = -d  # 此时记得将d取反
        min_part = min(left_part, right_part)
        d = left_part - right_part

    return ''.join(string)


def rotate(string: List[str], left: int, right: int, size: int):
    right_index = right-size+1  # 该函数的作用是string='abcdefg' size=3 得到'efgabcd' 而不是进行逆序
    while right_index <= right:
        temp = string[left]
        string[left] = string[right_index]
        string[right_index] = temp
        left += 1
        right_index += 1

    return string


def reverse(string: List[str], left: int, right: int):
    while left < right:
        temp = string[left]
        string[left] = string[right]
        string[right] = temp
        left += 1
        right -= 1

    return string


if __name__ == "__main__":
    num = int(input())
    test = list(input())
    print(rotate_word_2(test, num))
