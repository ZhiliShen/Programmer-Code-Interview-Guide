# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-09 16:36
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def merge_sort(array: list):
    aux = [0 for _ in range(len(array))]
    sort(array, aux, 0, len(array) - 1)


def sort(array: list, aux: list, low: int, high: int):
    if high <= low:
        return
    mid = low + (high - low) // 2
    sort(array, aux, low, mid)
    sort(array, aux, mid + 1, high)
    merge(array, aux, low, mid, high)


def merge(array: list, aux: list, low: int, mid: int, high: int):
    for index in range(low, high+1):
        aux[index] = array[index]

    i, j = low, mid + 1
    for index in range(low, high+1):   # 这里index的取值范围需要注意
        if i > mid:
            array[index] = aux[j]  # 这里是array等于aux 不是array等于array!
            j += 1
        elif j > high:
            array[index] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            array[index] = aux[j]
            j += 1
        else:
            array[index] = aux[i]
            i += 1


def get_small_sum(array: list):
    array_len = len(array)
    if array_len == 0:
        return 0
    aux = [0 for _ in range(array_len)]
    return func(array, aux, 0, array_len-1)


def func(array: list, aux: list, low: int, high: int):
    if high <= low:
        return 0
    mid = low + (high-low)//2
    return func(array, aux, low, mid) + func(array, aux, mid+1, high) + merge_small_sum(array, aux, low, mid, high)


def merge_small_sum(array: list, aux: list, low: int, mid: int, high: int):
    for index in range(low, high+1):
        aux[index] = array[index]

    i, j = low, mid+1  # 这里i是low 不是0！
    res = 0
    for index in range(low, high+1):
        if i > mid:
            array[index] = aux[j]
            j += 1
        elif j > high:
            array[index] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            array[index] = aux[j]
            j += 1
        else:  # 每次在归并操作出现左边的数字小于等于右边的数字 就累计左边的数字*右边的数字右边的数字的数目(包括自己)
            res += aux[i] * (high - j + 1)  # 先累计res 再去自增i 顺序颠倒之后你以为的aux[i]就不是你想的aux[i]!
            array[index] = aux[i]
            i += 1
    return res


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(get_small_sum(test))
