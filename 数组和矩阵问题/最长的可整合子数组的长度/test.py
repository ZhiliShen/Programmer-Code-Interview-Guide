# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-12 09:59
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def quick_sort(array: list, start: int, end: int):
    if end <= start:
        return
    mid = partition_1(array, start, end)
    quick_sort(array, start, mid - 1)
    quick_sort(array, mid + 1, end)


def partition_1(array: list, start: int, end: int):
    flag = array[start]
    i = start
    j = end + 1
    while True:
        while True:
            i += 1
            if array[i] >= flag:
                break
            if i == end:
                break
        while True:
            j -= 1
            if array[j] <= flag:
                break
            if j == start:
                break
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
    array[start], array[j] = array[j], array[start]
    return j


def partition_2(array: list, start: int, end: int):
    flag = array[end]
    i = start - 1
    for j in range(start, end + 1):
        if array[j] <= flag:  # 这里是小于等于 这样才能保证flag回到中间位置
            i += 1
            array[i], array[j] = array[j], array[i]

    return i


def get_longest_integrated_sequence_1(array: list):
    if array is None or len(array) == 0:
        return 0

    res = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if valid_integrated_1(array, i, j):
                res = max(res, j - i + 1)

    return res


def valid_integrated_1(array: list, start: int, end: int):
    aux = []
    for num in array[start:end + 1]:
        aux.append(num)
    quick_sort(aux, 0, len(aux) - 1)
    for i in range(1, len(aux)):
        if aux[i] != aux[i - 1] + 1:
            return False
    return True


def get_longest_integrated_sequence_2(array: list):
    if array is None or len(array) == 0:
        return 0

    res = 0
    num_in_cur_array = set()
    for i in range(len(array)):
        max_num = -float("inf")  # i更新的时候 max_num与min_num也都需要更新
        min_num = float("inf")
        for j in range(i, len(array)):  # 我一开始想的是每次都要将[i:j]都放进新的set 但是其实没必要 因为新的相比原来的只是多了一个元素而已
            if array[j] in num_in_cur_array:  # 如果出现一次重复元素 则整个后面其实都不用看了
                break
            num_in_cur_array.add(array[j])
            max_num = max(max_num, array[j])
            min_num = min(min_num, array[j])
            if max_num - min_num == j - i:  # 如果最大元素与最小元素的差值等于元素个数减一 则说明这个数组是逐渐递增1的
                res = max(res, j - i + 1)
        num_in_cur_array.clear()

    return res


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(get_longest_integrated_sequence_2(test))
