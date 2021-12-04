# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-04 21:52
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import random


def print_rand_m(array: list, m: int):
    m = min(len(array), m)
    count = 0
    while count < m:
        index = int(random.random()*(len(array)-count))
        print(array[index])
        array[index], array[-1-count] = array[-1-count], array[index]   # 注意这里的用于存放已经输出过的元素的位置是要更新的
        count += 1


if __name__ == "__main__":
    print_rand_m(list(range(100)), 10)
