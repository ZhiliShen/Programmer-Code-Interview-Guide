# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-09 20:57
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def max_sum(array: list):
    array_len = len(array)
    if array_len == 0:
        return 0
    res = -float("inf")
    cur = 0
    for num in array:
        cur += num
        res = max(cur, res)
        if cur < 0:
            cur = 0
    return res


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(max_sum(test))