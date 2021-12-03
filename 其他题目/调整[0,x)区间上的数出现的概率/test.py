# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-03 10:37
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import random


def rand_x_pow_k(k: int):
    if k < 1:
        return 0
    res = max([random.random() for _ in range(k)])  # 注意这里使用max函数
    return res


if __name__ == "__main__":
    print(rand_x_pow_k(3))
