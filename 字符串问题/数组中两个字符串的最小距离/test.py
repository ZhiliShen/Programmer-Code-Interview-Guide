# -*- coding: utf-8 -*- #
# @Time    : 2021-10-17 16:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def min_distance_1(chars: List[str], a_char: str, b_char: str):
    if len(chars) <= 1:
        return -1
    if a_char == b_char:
        return 0
    result = float('inf')
    last_a_char = -1
    last_b_char = -1
    for index, char in enumerate(chars):
        if char == a_char:
            last_a_char = index
            if last_b_char != -1:
                result = min(result, last_a_char - last_b_char)
        if char == b_char:
            last_b_char = index
            if last_a_char != -1:
                result = min(result, last_b_char - last_a_char)

    return -1 if result == float('inf') else result


class Record:
    def __init__(self, chars: List[str]):
        self.chars = chars
        self.char2char_map = {}  # 形为{1: {3: 2}} 依次为a_char b_char 以及两者之间的最近距离
        self.char2last_map = {}  # 形为{1: 2} 依次为char 以及该char最近一次出现的位置
        for index, char in enumerate(chars):
            self.update(char, index)  # 每一次遍历 就需要更新char2char_map
            self.char2last_map[char] = index  # 每一次遍历 就需要更新其最近一次出现的位置

    def update(self, char: str, index: int):
        char2min_map = self.char2char_map.get(char, None)
        if char2min_map is None:  # 如果当前的char2char_map没有该字符则新建一个 并将其添加进char2char_map
            char2min_map = {}
            self.char2char_map[char] = char2min_map
        for key, value in self.char2last_map.items():  # 开始计算当前字符与之前字符的最短距离
            if key != char:  # 不需要更新其与自己的最短距离
                min_distance = index - value  # 计算当前字符与之前字符的现有最短距离
                char2min = char2min_map.get(key, None)  # 取出当前字符与这个之前字符之前的最短距离
                another_char2min = self.char2char_map[key]  # 有1: {3: 2}必有3: {1: 2} 需要同步更新 而且不用担心其没有 出现在char2last_map 必出现在char2char_map
                if char2min is None:  # 如果当前字符与这个之前字符不存在最短距离 则直接记录
                    char2min_map[key] = min_distance
                    another_char2min[char] = min_distance
                else:  # 否则取其中较小的进行记录
                    if min_distance < char2min:
                        char2min_map[key] = min_distance
                        another_char2min[char] = min_distance

    def min_distance(self, a_char: str, b_char: str):
        if a_char == b_char:
            return 0
        if self.char2char_map.get(a_char, None) is not None and self.char2char_map[a_char].get(b_char,
                                                                                               None) is not None:
            return self.char2char_map[a_char][b_char]
        return -1


if __name__ == "__main__":
    num = int(input())
    target_a, target_b = input().split()
    test = []
    for _ in range(num):
        temp = input()
        test.append(temp)
    record = Record(test)
    print(record.min_distance(target_a, target_b))
