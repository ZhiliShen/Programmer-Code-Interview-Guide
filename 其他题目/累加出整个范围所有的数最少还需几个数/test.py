# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-04 14:19
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

def min_needs(array: list, target_range: int):
    array.sort()
    cur_range = 0
    index = 0
    need_nums = 0
    while cur_range < target_range and index < len(array):
        while cur_range < array[index] - 1:  # 如果当前的覆盖范围不足以达到该位置的需要
            cur_range += (cur_range+1)  # 则需要补充cur_range+1的数字进去
            need_nums += 1  # 需要补充的数字加1
            if cur_range >= target_range:  # 因为array[index]可能大于目标范围 所以没必要一定要到array[index] 中途大于目标范围即可退出
                return need_nums
        cur_range += array[index]
        index += 1

    if cur_range >= target_range:  # 如果是因为达到目标而退出 则直接返回需要补充的数字的数目
        return need_nums

    while cur_range < target_range:  # 如果数组遍历完了还没有达到要求 则继续补充cur_range+1的数字直到完成任务
        cur_range += (cur_range + 1)
        need_nums += 1
    return need_nums


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print(min_needs(test, b))
