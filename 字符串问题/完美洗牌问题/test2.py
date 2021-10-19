# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-14 19:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
from typing import List


# 堆排序在最坏的情况下仍能保证~2NlgN次比较和常数级别的额外空间 但由于其元素很少与相邻的其他元素进行比较 所以其缓存命中的次数要远远小于其他比较都在相邻元素间进行的排序算法 例如快速排序 归并排序与希尔排序
# 当用于表示堆的数组是从1开始的 则k节点的子节点分别为2*k与2*k+1 其父节点为k//2
# 当用于表示堆的数组是从0开始的 则k节点的子节点分别为2*k+1与2*k+2 其父节点为(k-1)//2
def heap_sort(array: List):
    length = len(array)
    if length <= 1:
        return
    # 堆的构造 此阶段需要少于2N次比较
    # 关于堆的构造 可以选择从左到右遍历数组 对每个元素进行上浮操作 以保证每一轮i的左侧都是堆有序的
    # 也可以选择从右到左遍历数组 对每个元素进行下沉操作 以保证每一轮i的右侧都是堆有序的 这样的好处是不用写上浮操作函数
    # 而且由于数组的右半部分均代表大小为1的子堆 必然已经堆有序 所以我们可以从数组的右半部分开始往左遍历
    # 但是一定是从中间到0 而不是0到中间 方向不能弄错 核心原因是因为无论是下沉操作也好 上浮操作也罢 一定要保证当前视作堆的范围一定是堆有序的
    # 至于从哪里开始往左 则需要找到最后一个大小为2的堆 计算方式就是((length-1)-1)//2->length//2-1
    for i in range(length // 2 - 1, -1, -1):
        sink(array, i, length)
    # 下沉排序 此阶段需要2NlgN 因为每次下沉都可能需要2lgN次比较
    # 下沉排序阶段需要告诉swap数组的哪一部分是堆 而之外的部分则是已经排好序的内容 并且其是左闭右开
    # 堆有序的数组往往右边都比较小 而我们交换时会把右边的数字提到堆顶 而它们的归宿往往又是堆底 所以可以直接将较大的子节点提升 直到该元素到达堆底 再进行上浮操作 可以有效减少比较次数
    for i in range(length):
        swap(array, 0, length - 1 - i)  # 这里swap与sink的均是数组的首个元素 而不是像建堆时关注的是i
        sink(array, 0, length - 1 - i)


def sink(array: List, index: int, end: int):
    while index * 2 + 1 < end:
        child_index = index * 2 + 1
        # 且运算的短路操作能保证数组不会越界 下沉操作选较大的进行比较 你连小弟中最厉害的都打不过 那你就不配当大哥
        if child_index + 1 < end and array[child_index] < array[child_index + 1]:
            child_index += 1
        if array[index] < array[child_index]:
            swap(array, index, child_index)
        else:
            break
        index = child_index  # 写while循环不要忘记对标志量进行操作


def swap(array: List, i: int, j: int):
    array[i], array[j] = array[j], array[i]


def shuffle(array: List, length: int):
    if length <= 1:
        return array
    heap_sort(array)
    # 先进行排序 123456->132546 即可
    for i in range(0, length-2, 2):
        swap(array, i+1, i+2)

    return array


if __name__ == "__main__":
    num = int(input())
    test = list(map(int, input().split()))
    print(' '.join(map(str, shuffle(test, num))))
