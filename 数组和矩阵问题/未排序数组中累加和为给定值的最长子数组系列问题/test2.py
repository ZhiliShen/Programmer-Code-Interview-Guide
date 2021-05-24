# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-23 19:53
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
import sys
from typing import List


def max_length(arr: List, k: int):
    if arr is None or len(arr) == 0:
        return 0
    dic = {0: -1}
    temp_sum = 0
    max_len = 0
    for i, cur in enumerate(arr):
        temp_sum += cur
        dic.setdefault(temp_sum, i)
        j = dic.get(temp_sum-k)
        if j is not None:
            max_len = max(i-j, max_len)
    return max_len


if __name__ == "__main__":
    for idx, line in enumerate(sys.stdin):
        if idx == 0:
            temp = [int(k) for k in line.split()]
            length = temp[0]
        elif idx == 1:
            temp = []
            old_temp = [int(k) for k in line.split()]
            for cur in old_temp:
                if cur < 0:
                    temp.append(-1)
                elif cur == 0:
                    temp.append(0)
                else:
                    temp.append(1)
            break

    print(max_length(temp, 0))
