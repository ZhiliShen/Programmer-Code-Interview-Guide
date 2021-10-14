# -*- coding: utf-8 -*- #
# @Time    : 2021-10-13 21:07
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
from typing import List


def rotate_word_1(string: List[str]):
    length = len(string)
    if length == 0:
        return

    reverse(string, 0, length - 1)

    left, right = -1, -1
    for i in range(length):  # 我们通常会以空格符作为标识符 一旦遇到空格符 则对上一阶段所记录的词汇进行翻转 但最后一个词汇后面是没有空格的 所以怎样优雅地处理最后一个词汇是很重要的点
        # 尝试过对i进行判断 一旦i走到末尾 就进行翻转 但一旦最后一个词是一个字符处理起来会比较麻烦 所以将left与right初始时设置为-1 只有在必要的时候更新 每次更新完后 检查两者是否都进行了更新 一旦都进行了更新 则开始翻转
        if string[i] != ' ':
            left = i if (i == 0 or string[i - 1] == ' ') else left  # 或运算的短路特性使得其不会出现数组越界的情况
            right = i if (i == length-1 or string[i + 1] == ' ') else right  # 与上同理
        if left != -1 and right != -1:
            reverse(string, left, right)
            left, right = -1, -1

    return "".join(string)


def rotate_word_2(string: List[str]):
    length = len(string)
    if length == 0:
        return

    left, right = -1, -1
    for i in range(length):
        if string[i] != ' ':
            left = i if (i == 0 or string[i-1] == ' ') else left
            right = i if (i == length-1 or string[i+1] == ' ') else right
        if left != -1 and right != -1:
            reverse(string, left, right)
            left, right = -1, -1

    return ''.join(string)


def reverse(string: List[str], left, right):
    if len(string) == 0:
        return

    while left < right:
        temp = string[left]
        string[left] = string[right]
        string[right] = temp
        left += 1  # while循环一定要对标志量进行处理
        right -= 1


if __name__ == "__main__":
    test = input()
    print(rotate_word_2(list(test)))
