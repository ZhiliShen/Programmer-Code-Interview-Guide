# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-29 21:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import random


def rand(max_num: int):
    return int(random.random()*max_num)+1


def get_k_nums_rand(k: int, len_nums: int):
    if k < 1 or len_nums < 1:
        return None
    res = [0 for _ in range(min(k, len_nums))]
    for index in range(len(res)):  # 将前k个数直接进入数组中
        res[index] = index+1
    for index in range(k+1, len_nums+1):
        if rand(index) <= k:  # 决定index是否进入数组 概率为k/当前处理的元素的序号
            res[rand(k)-1] = index  # 随机决定数组中的某一个元素被替换
    return res


if __name__ == "__main__":
    print(get_k_nums_rand(10, 100))
