# -*- coding: utf-8 -*- #
# @Time    : 2021-11-09 16:10
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def max_product(array: List[int]):
    if len(array) == 0:
        return 0
    res, cur_max_end, cur_min_end = array[0], array[0], array[0]

    for num in array[1:]:
        pre_max_end, pre_min_end = cur_max_end, cur_min_end
        # 以当前数字结尾的最大子数组积有三种选择 以前一个数字结尾的最大子数组积乘以当前数字 以前一个数字结尾的最小子数组积乘以当前数字 当前数字
        cur_max_end = max(pre_max_end * num, pre_min_end * num, num)
        cur_min_end = min(pre_max_end * num, pre_min_end * num, num)  # 确保现在使用的变量没有在之前受到没有意识到的改动
        res = max(res, cur_max_end)

    return res


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(float, input().split()))
    print('%.2f' % max_product(test))
