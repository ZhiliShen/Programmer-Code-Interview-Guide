# -*- coding: utf-8 -*- #
# @Time    : 2021/11/12 22:10
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
def partition(array: list):
    if array is None or len(array) < 2:
        return
    left, index, right = -1, 0, len(array)
    while index < right:
        if array[index] == 0:
            left += 1
            array[left], array[index] = array[index], array[left]
            index += 1
        elif array[index] == 1:
            index += 1
        else:
            right -= 1
            array[right], array[index] = array[index], array[right]


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    partition(test)
    print(*test)