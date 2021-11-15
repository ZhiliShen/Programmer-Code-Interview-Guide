# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-15 13:41
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :

def print_half_major(array: list):
    times = 0
    candidate = 0
    for num in array:
        if times == 0:  # 如果当前times为0 则两个候选数都已经被删完了
            candidate = num
        elif num != candidate:  # 如果当前数与上一个数不相同 则将两个数同时删除
            times -= 1
        else:  # 如果当前数和候选数一样 则计数器加1
            times += 1

    candidate_num = 0
    for num in array:  # 像[1, 2, 3]这种情况 最后剩下来的是3 但是3并不符合要求 所以需要进行一次额外的检验
        if num == candidate:
            candidate_num += 1
    if 2 * candidate_num < len(array):
        return -1
    else:
        return candidate


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(print_half_major(test))
