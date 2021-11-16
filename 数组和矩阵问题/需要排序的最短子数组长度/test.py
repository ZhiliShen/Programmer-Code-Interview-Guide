# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-16 13:49
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def get_min_length(array: list):
    if array is None or len(array) < 2:
        return 0

    # 记录右侧出现过的最小值 并找到最左边的大于右侧出现过的最小值的位置 因为要变为有序则必然需要将该位置移动到右侧出现过的最小值的右边
    right_min, bigger_than_right_min = array[-1], -1
    for i in range(len(array) - 2, -1, -1):
        if array[i] > right_min:
            bigger_than_right_min = i
        else:
            right_min = array[i]

    # 如果找不到 则说明数组本身就是有序的
    if bigger_than_right_min == -1:
        return 0

    # 记录左侧出现过的最大值 并找到最右边的小于左侧出现过的最大值的位置 因为要变为有序则必然需要将该位置移动到左侧出现过的最大值的左边
    left_max, less_than_left_max = array[0], -1
    for i in range(1, len(array)):
        if array[i] < left_max:
            less_than_left_max = i
        else:
            left_max = array[i]

    return less_than_left_max - bigger_than_right_min + 1


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(get_min_length(test))
