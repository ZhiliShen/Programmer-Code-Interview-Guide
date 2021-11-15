# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-15 10:33
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :

def print_unique_pair(array: list, k: int):
    if array is None or len(array) < 2:
        return

    left, right = 0, len(array) - 1  # 双指针的好处就在于打印出的顺序是满足题目中对于顺序的要求
    while left < right:
        if array[left] + array[right] < k:
            left += 1
        elif array[left] + array[right] > k:
            right -= 1
        else:
            if left == 0 or array[left] != array[left-1]:
                print(array[left], array[right])
            left += 1  # 一定要放在if之外
            right -= 1  # 循环中始终不要忘记对标志量进行变化


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print_unique_pair(test, b)
