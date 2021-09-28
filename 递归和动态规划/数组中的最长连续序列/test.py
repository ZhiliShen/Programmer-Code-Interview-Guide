# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-28 18:41
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def dynamic_programming(array: List[int]):
    hash_map = {}
    max_length = 1
    for num in array:
        if hash_map.get(num, None) is None:
            hash_map[num] = 1  # 当字典中不存在该数组时 其有可能扩展现有最长连续子序列的边界
            if hash_map.get(num - 1, None) is not None:
                max_length = max(max_length, merge(hash_map, num - 1, num))
            if hash_map.get(num + 1, None) is not None:
                max_length = max(max_length, merge(hash_map, num, num + 1))

    return max_length


def merge(hash_map: dict, less: int, more: int):  # merge函数的位置就已经能够清晰表明哪一段是左边界 哪一段是右边界
    less_length = hash_map[less]
    more_length = hash_map[more]
    new_length = less_length + more_length
    hash_map[less - less_length + 1] = new_length
    hash_map[more + more_length - 1] = new_length

    return new_length


if __name__ == "__main__":
    n = int(input())
    test = [int(k) for k in input().split()]  # 可以将一个有分隔符的数字字符串的每一位拆分出来
    print(dynamic_programming(test))
