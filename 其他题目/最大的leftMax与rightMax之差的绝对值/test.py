# -*- coding: utf-8 -*- #
# @Time    : 2021/11/29 23:17
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

def max_abs(array: list):
    res = -float("inf")
    arr_len = len(array)
    for split_index in range(0, arr_len - 1):
        left_max = -float("inf")
        right_max = -float("inf")
        for num in array[0:split_index + 1]:
            left_max = max(left_max, num)
        for num in array[split_index + 1:]:
            right_max = max(right_max, num)
        res = max(res, abs(left_max - right_max))
    return res


# 数组的预处理是空间换时间的一种体现
def max_abs_1(array: list):
    res = -float("inf")
    arr_len = len(array)
    left_max = [0 for _ in range(arr_len)]  # left_max[i]表示array[0~i]中的最大值
    right_max = [0 for _ in range(arr_len)]  # right_max[i]表示array[i~N-1]中的最大值
    left_max_count = -float("inf")
    right_max_count = -float("inf")
    for index in range(arr_len):
        left_max_count = max(left_max_count, array[index])
        left_max[index] = left_max_count
    for index in range(arr_len - 1, -1, -1):
        right_max_count = max(right_max_count, array[index])
        right_max[index] = right_max_count
    for split in range(arr_len - 1):
        res = max(res, abs(left_max[split] - right_max[split + 1]))
    return res


# 整个数组的最大值要么是左半部分的最大值 要么是右半部分的最大值
# 若整个数组的最大值为左半部分的最大值 则希望右半部分的最大值尽可能的小 而右半部分的最大值是一个随分割位置增大而不增大的函数 因此当右半部分只含有末尾的时候 是右半部分的最大值最小的时候
# 若整个数组的最大值为右半部分的最大值 则希望左半部分的最大值尽可能的小 而左半部分的最大值是一个随分割位置增大而不减小的函数 因此当左半部分只含有开头的时候 是左半部分的最大值最小的时候
def max_abs_2(array: list):
    max_count = max(array)
    return max(abs(max_count - array[-1]), abs(array[0] - max_count))


if __name__ == "__main__":
    a = input()
    test = list(map(int, input().split()))
    print(max_abs_2(test))
