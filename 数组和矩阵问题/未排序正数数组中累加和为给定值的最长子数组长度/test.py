# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-15 15:24
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

def get_max_length(array: list, k: int):
    if array is None or len(array) < 1 or k <= 0:
        return 0
    left, right = 0, 0
    cur_sum = array[left]
    res = 0
    while right < len(array):
        if cur_sum == k:  # 如果此时区间段的和已经等于k 因为是正数数组 所以right后面的不用再检查
            res = max(res, right - left + 1)
            cur_sum -= array[left]  # 此时right不用回退 因为此区间段的和等于k 所以right前面的区间段不可能等于k
            left += 1
        elif cur_sum < k:
            right += 1
            if right == len(array):  # 一定要检查数组的合法性
                break
            cur_sum += array[right]
        else:
            cur_sum -= array[left]
            left += 1

    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print(get_max_length(test, b))
