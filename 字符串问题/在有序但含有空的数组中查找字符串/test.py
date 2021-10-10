# -*- coding: utf-8 -*- #
# @Time    : 2021-10-08 20:35
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def get_index(cur: List[str], target: str):
    left = 0
    right = len(cur)  # 区间段是[left0, left)是小于target, [right, right0)是大于等于target
    while left < right:
        mid = left + (right - left) // 2
        if cur[mid] is None:
            for i in range(mid, left-1, -1):
                if cur[i] is not None:
                    if cur[i] < target:
                        left = i+1
                        break
                    if cur[i] >= target:
                        right = i
                        break
            else:  # python语法糖 如果for循环没有因为break而跳出 那么就执行else中的语句 要不然则不执行
                left = mid + 1
        else:
            if cur[mid] < target:
                left = mid + 1
            if cur[mid] >= target:

                right = mid
    return right if (cur[right] is not None and cur[right] == target) else -1


if __name__ == "__main__":
    num = int(input())
    target_str = input()
    test = []
    for _ in range(num):
        temp = input()
        if temp == '0':
            test.append(None)
        else:
            test.append(temp)
    print(get_index(test, target_str))
