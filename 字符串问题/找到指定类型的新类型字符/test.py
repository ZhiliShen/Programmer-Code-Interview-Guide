# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-25 18:22
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def point_new_char(chars: str, index: int):
    chars_len = len(chars)
    if chars_len == 0 or index < 0 or index >= chars_len:
        return ''
    upper_num = 0
    # 从index-1开始往左边走 走到是小写字母为止 统计该区间段内只有大写字母 并统计大写字母个数
    for i in range(index-1, -1, -1):
        if chars[i].islower():
            break
        upper_num += 1
    if (upper_num & 1) == 1:  # 大写字母个数是奇数 说明index-1,index是一个整体
        return chars[index-1:index+1]
    else:
        if chars[k].isupper():  # 大写字母个数是偶数 当前字母是大写 说明index,index+1是一个整体
            return chars[index:index+2]
        else:  # 大写字母个数是偶数 当前字母是小写 说明index是一个整体
            return chars[index]


if __name__ == "__main__":
    n, k = map(int, input().split())
    test = input()
    print(point_new_char(test, k))
