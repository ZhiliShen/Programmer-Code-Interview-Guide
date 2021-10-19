# -*- coding: utf-8 -*- #
# @Time    : 2021-10-18 20:16
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


# i->2*i+1, 2*i+2 | i->(i-1)//2
def heap_sort(array: list):
    length = len(array)
    if length <= 1:
        return
    for i in range(((length - 1) - 1) // 2, -1, -1):
        sink(array, i, length)
    for i in range(length):
        array[0], array[length - 1 - i] = array[length - 1 - i], array[0]
        sink(array, 0, length - 1 - i)


def sink(array: list, index: int, end: int):
    while 2 * index + 1 < end:
        child_index = 2 * index + 1
        if child_index + 1 < end and array[child_index] < array[child_index + 1]:
            child_index += 1
        if array[index] < array[child_index]:
            array[index], array[child_index] = array[child_index], array[index]
            index = child_index
        else:
            break


def is_unique_1(chars: List[int]):
    char_map = {}
    for char in chars:
        if char_map.get(char, False):
            return 'NO'
        char_map[char] = True

    return 'YES'


def is_unique_2(chars: List[int]):
    heap_sort(chars)
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            return 'NO'

    return 'YES'


if __name__ == "__main__":
    n = input()
    test = list(map(int, input().split()))
    print(is_unique_2(test))
