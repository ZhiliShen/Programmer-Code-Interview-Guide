# -*- coding: utf-8 -*- # 
# @Time    : 2021-06-06 19:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from 二叉树问题.utils.utils import print_list


def search(s: str, p: str):
    if s is None or p is None or len(s) < len(p):
        return [-1]
    result = []
    dfa = get_dfa(p)
    s_index, p_index = 0, 0
    while s_index < len(s):
        if p_index == -1 or s[s_index] == p[p_index]:
            s_index += 1
            p_index += 1
            if p_index == len(p):
                result.append(s_index - p_index)
                p_index = dfa[p_index]
        else:
            p_index = dfa[p_index]
    if len(result) == 0:
        return [-1]
    else:
        return result


def get_dfa(p: str):
    dfa = [None for i in range(len(p)+1)]
    dfa[0] = -1
    if len(dfa) == 1:
        return dfa
    dfa[1] = 0
    index, before_index_substr_max_len = 2, 0
    while index <= len(p):
        if before_index_substr_max_len == -1 or p[index - 1] == p[before_index_substr_max_len]:
            before_index_substr_max_len += 1
            dfa[index] = before_index_substr_max_len
            index += 1
        else:
            before_index_substr_max_len = dfa[before_index_substr_max_len]
    return dfa


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    m = sys.stdin.readline().strip()

    print_list(search(s, m))

