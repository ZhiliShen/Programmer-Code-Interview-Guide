# -*- coding: utf-8 -*- #
# @Time    : 2021-09-21 20:01
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def dynamic_programming(array: List[int]):
    length = len(array)
    if length == 0:
        return 0
    dp = [None for i in range(length)]

    # base case:
    dp[0] = 1

    # transfer equation:
    for i in range(1, length):
        dp[i] = 1
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_len = 0
    max_index = 0
    for index, num in enumerate(dp):
        if num > max_len:
            max_len = num
            max_index = index

    return generate_lis(array, dp, max_len, max_index)


def dynamic_programming_with_binary_search(array: List[int]):
    length = len(array)
    if length == 0:
        return 0

    dp = [None for i in range(length)]  # 以array[i]结尾的最长递增子序列的长度
    ends = [None for i in range(length)]  # 在所有长度为i+1的递增子序列的结尾数字中最小的那一个数字 该数组是严格递增的
    right = 0  # 当前ends已经记录的有效范围是[:right]

    dp[0] = 1
    ends[0] = array[0]

    max_index = 0  # 记录当前最长递增子序列的结尾数字的索引

    for index in range(1, length):
        lower_bound = binary_search(ends, right, array[index])  # 这里要传参的数组是ends! 需要第一个大于等于target的index 即寻求下界
        if lower_bound == right + 1:  # 如果结果是在数组的合法范围之外 说明可以扩增递增子序列 如果扩增的话 则需要初始化max_index
            right += 1
            max_index = index
        ends[lower_bound] = array[index]  # 这里应该取lower_bound!
        dp[index] = lower_bound+1  # 这里应该取lower_bound!
        if lower_bound == right:  # 如果更新的正好是当前最长的递增子序列 则需要更新max_index 而且更新后的max_index对应的字典和一定是最小的
            max_index = index

    return generate_lis(array, dp, right+1, max_index)


def binary_search(ends: List[int], right, num):
    lo = 0
    hi = right + 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if ends[mid] < num:
            lo = mid + 1
        else:
            hi = mid
    return hi


def generate_lis(array: List[int], dp: List[int], max_len, max_index):
    lis = [None for i in range(max_len)]

    max_len -= 1
    lis[max_len] = array[max_index]

    for i in range(max_index - 1, -1, -1):  # 写一个for循环就可以了
        if dp[i] == dp[max_index] - 1 and array[i] < array[max_index]:
            max_len -= 1  # 时刻注意长度到索引之间的转换
            lis[max_len] = array[i]
            max_index = i  # 内部max_index的改变并不会影响外面以max_index作为边界的for循环的次数

    return " ".join([str(i) for i in lis])


if __name__ == "__main__":
    n = int(input())
    test = [int(k) for k in input().split()]  # 可以将一个有分隔符的数字字符串的每一位拆分出来
    print(dynamic_programming_with_binary_search(test))
