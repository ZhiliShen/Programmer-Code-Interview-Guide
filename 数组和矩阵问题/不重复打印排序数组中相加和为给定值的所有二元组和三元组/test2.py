# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-15 10:43
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :


def print_unique_triad(array: list, k: int):
    if array is None or len(array) < 3:
        return

    for index, num in enumerate(array[:-2]):
        if index == 0 or array[index] != array[index - 1]:
            print_unique_pair(array, k - num, index, index + 1, len(array) - 1)


def print_unique_pair(array: list, k: int, index: int, left: int, right: int):
    while left < right:
        if array[left] + array[right] < k:
            left += 1
        elif array[left] + array[right] > k:
            right -= 1
        else:
            # if (left == index+1 or array[left] != array[left-1]) and array[left] != array[index] and array[right] != array[left]:  # 此行代码是为了确保严格升序
            if left == index+1 or array[left] != array[left-1]:
                print(array[index], array[left], array[right])
            left += 1  # 一定要放在if之外
            right -= 1  # 循环中始终不要忘记对标志量进行变化


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print_unique_triad(test, b)
