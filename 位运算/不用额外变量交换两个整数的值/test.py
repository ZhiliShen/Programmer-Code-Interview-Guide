# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-11 16:43
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def swap(a_num: int, b_num: int):
    a_num = a_num ^ b_num
    b_num = b_num ^ a_num
    a_num = a_num ^ b_num
    return a_num, b_num


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(*swap(a, b))
