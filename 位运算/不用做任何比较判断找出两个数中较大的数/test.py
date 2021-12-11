# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-11 16:47
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def flip(num: int):  # 如果num是0 则返回1 如果num是1 则返回0
    return num ^ 1


def sign(num: int):  # 如果num是自然数 则返回1 如果num是负数 则返回0
    return flip((num >> 31) & 1)


def get_max(a_num: int, b_num: int):
    c_num = a_num - b_num  # 但这里可能会出现溢出问题
    sign_a = sign(c_num)  # 如果差值为自然数 则sign_a为1 则说明a是较大的
    sign_b = flip(sign_a)  # 如果差值为负数 则sign_b为1 则说明b是较大的
    return sign_a * a_num + sign_b * b_num

def get_max_1(a_num, b_num):
    c_num = a_num - b_num
    sign_a = sign(a_num)
    sign_b = sign(b_num)
    sign_c = sign(c_num)
    is_ab_diff = sign_a ^ sign_b  # 用于判断a_num与b_num是否是不同符号
    is_ab_same = flip(is_ab_diff)  # 用于判断a_num与b_num是否是相同符号
    # 如果a_num与b_num的符号不同 即is_ab_diff是1 is_ab_same是0
    # 则如果a为自然数 那么b为负数 则应当返回a
    # 则如果a为负数 那么b为自然数 则应当返回b
    # 如果a_num与b_num的符号相同 则c_num绝对不会溢出 直接按照原有方式继续处理
    # 所以返回a_num的情况是is_ab_diff*sign_a+is_ab_same*sign_c
    # 否则就返回b_num
    return a_num*(is_ab_diff*sign_a+is_ab_same*sign_c) + b*flip(is_ab_diff*sign_a+is_ab_same*sign_c)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(get_max_1(a, b))
