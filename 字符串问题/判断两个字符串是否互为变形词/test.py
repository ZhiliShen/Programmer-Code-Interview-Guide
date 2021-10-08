# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-08 19:15
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def is_deformation(a_str, b_str):
    if len(a_str) != len(b_str):
        return 'false'
    char_map = [0 for i in range(256)]
    for temp in a_str:
        char_map[ord(temp)] += 1
    for temp in b_str:
        char_map[ord(temp)] -= 1
        if char_map[ord(temp)] < 0:  # 边遍历边检验
            return 'false'

    return 'true'


if __name__ == "__main__":
    a, b = map(int, input().split())
    str1 = input()
    str2 = input()
    print(is_deformation(str1, str2))
