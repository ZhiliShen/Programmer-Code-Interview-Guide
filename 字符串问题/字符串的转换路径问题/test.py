# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-17 19:56
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from collections import deque


def get_next_map(chars: List[str]):
    words_in_list = set(chars)
    next_map = {}
    for char in chars:
        next_map[char] = get_next_array(char, words_in_list)

    return next_map


def get_next_array(word: str, words_in_list: set):
    next_array = []
    word_list = list(word)
    for i in range(ord('a'), ord('z') + 1):
        for j in range(len(word_list)):
            if word_list[j] != chr(i):
                temp = word_list[j]
                word_list[j] = chr(i)
                if ''.join(word_list) in words_in_list:
                    next_array.append(''.join(word_list))
                word_list[j] = temp

    return next_array


def get_distance(start: str, next_map: dict):
    distance_map = {start: 0}
    queue = deque()
    queue.append(start)
    words_dealt = set()
    words_dealt.add(start)  # 不要忘记对已经处理的单词初始化
    while len(queue) != 0:
        cur_word = queue.popleft()
        for neighbour in next_map[cur_word]:
            if neighbour not in words_dealt:
                queue.append(neighbour)
                distance_map[neighbour] = distance_map[cur_word] + 1  # 直接在原距离的基础上+1
                words_dealt.add(neighbour)

    return distance_map


def get_shortest_paths(cur: str, end: str, next_map: dict, distance_map: dict, cur_path: List[str], result: List[str]):
    cur_path.append(cur)
    if cur == end:
        result.append(' -> '.join(cur_path))
    else:
        for neighbour in next_map[cur]:
            if distance_map[neighbour] == distance_map[cur] + 1:
                get_shortest_paths(neighbour, end, next_map, distance_map, cur_path, result)
    cur_path.pop()  # 不要忘记还原


def find_min_paths(start: str, end: str, chars: List[str]):
    chars.append(start)
    # 生成每个单词只需改变一个字母且在list中出现的变形词字典 形如{abc: [abb, cbc, acc]}
    next_map = get_next_map(chars)
    # 通过广度优先搜索生成list中每个单词到开头单词的最短距离
    distance_map = get_distance(start, next_map)
    cur_path, result = [], []
    # 通过深度优先遍历生成结果集 其实如果求最短距离 广度优先搜索已经能满足要求 但是如果需要记录最短路径有哪些 则需要先广度优先搜索 再深度优先搜索
    get_shortest_paths(start, end, next_map, distance_map, cur_path, result)
    return result


if __name__ == "__main__":
    num = int(input())
    a, b = input().split()
    test = []
    for _ in range(num):
        tmp = input()
        test.append(tmp)
    res = find_min_paths(a, b, test)
    if len(res) == 0:
        print('NO')
    else:
        print('YES')
        res.sort()
        for tmp in res:
            print(tmp)
