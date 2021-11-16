# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-16 19:35
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

# 该种解法的目的是希望在数组的左侧得到一个从1开始的排序数组 这个排序数组结束的位置右边的第一个位置就是缺失的第一个正数
def miss_num_1(array: list):
    # left表示当前array已经在[0,left-1]位置上形成了[1,2...,left]的连续增序数组
    # right表示当前array可能得到的连续数组的右边界
    # 举个例子 如果数组长度为6 则其可能得到的连续数组为123456 所以right取6
    left, right = 0, len(array)
    while left < right:
        # 如果当前数字的位置正好在其应该的地方 则left递增
        if array[left] == left + 1:
            left += 1
        # array[left]<=left 就表明当前的元素太小了 对于形成增序数组是没有帮助的 比如已经有[1,2,3] 这时候left指向的是1 没有办法形成增序数组 而且其存在影响了增序数组右边界尽可能增大的可能性
        # 例如[1,2,3,1,5] 由于右边的1的存在 导致了[1,2,3,4,5]这样的连续数组是不可能出现的 所以right要减小
        # array[left] > right 就表明当前元素太大了 对于形成增序数组是没有帮助的 比如已经有[1,2,3] 这时候left指向的是100 没有办法形成增序数组 而且其存在影响了增序数组右边界尽可能增大的可能性
        # 例如[1,2,3,100,5] 由于右边的1的存在 导致了[1,2,3,4,5]这样的连续数组是不可能出现的 所以right要减小
        # array[left] == array[array[left]-1] 就表明了当前元素有重复值 当前left指向的是合法的 但是在其应该放置的位置已经存在一个相同的数 所以进行同样的处理即可
        # 例如[2, 2]
        elif array[left] <= left or array[left] > right or array[left] == array[
            array[left] - 1]:  # 注意这里是array[left] <= left
            right -= 1
            array[left] = array[right]
        # 如果当前的元素是合法的 则将其放置到合理的位置 将合理位置上原来的元素取过来继续考察
        else:
            temp = array[array[left] - 1]
            array[array[left] - 1] = array[left]
            array[left] = temp

    # 已经排序好的连续增序数组的右边就是缺失的最小正整数
    return left + 1


# 该种解法的核心就是将那些在array中出现且范围在[1...len(array)]中的数字在对应的位置使用负数进行标记
# 那么第一个正数的位置就是缺失的位置
def miss_num_2(array: list):
    array_len = len(array)
    # 因为是使用了负数进行标记 所以第一个问题就是原来的负数会干扰我们判断 而这些负数和那些超出范围的数一样是没有用 所以直接把它们变为超出范围的数
    for i in range(array_len):
        if array[i] <= 0:
            array[i] = array_len + 1

    # 这个时候开始进行标记 在取数的时候因为 先前的数会把当前的数取反 所以需要取绝对值来得到原来真正的数
    for num in array:
        num = abs(num)
        if num <= array_len:
            array[num - 1] = -abs(array[num - 1])  # 进行取反

    # 寻找第一个正数出现的位置
    for i in range(len(array)):
        if array[i] > 0:
            return i + 1

    # 如果全部是负数 则说明其本身就是一个连续增序数组的乱序排列
    return len(array) + 1


# 该种解法与第一种解法类似 还是希望构建一个连续增序的数组
def miss_num_3(array: list):
    array_len = len(array)
    for i in range(len(array)):
        # 把每一个数字都放到正确的位置上 如果有重复的数字不用担心 因为总有一个会放到正确的位置上
        while 0 < array[i] <= array_len and array[i] != array[array[i] - 1]:
            temp = array[array[i]-1]
            array[array[i]-1] = array[i]
            array[i] = temp

    # 找到第一个位置不对的数字
    for i in range(len(array)):
        if array[i] != i+1:
            return i+1

    return array_len+1


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(miss_num_1(test))
