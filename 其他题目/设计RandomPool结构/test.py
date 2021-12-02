# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-02 14:44
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import random


class RandomPool:
    def __init__(self):
        self.key2index = {}
        self.index2key = {}
        self.size = 0

    def insert(self, key):
        if key not in self.key2index:
            self.key2index[key] = self.size
            self.index2key[self.size] = key
            self.size += 1

    def delete(self, key):
        if key in self.key2index:
            index = self.key2index[key]
            last_key = self.index2key[self.size-1]
            self.key2index[last_key] = index  # 通过对原始key的覆盖实现index的连续
            self.index2key[index] = last_key
            self.key2index.pop(key)
            self.index2key.pop(self.size-1)
            self.size -= 1

    def get_random(self):
        if self.size == 0:
            return None
        random_index = int(random.random()*self.size)
        return self.index2key[random_index]


if __name__ == "__main__":
    random_pool = RandomPool()
    random_pool.insert(1)
    random_pool.insert(2)
    random_pool.insert(3)
    random_pool.insert(4)
    random_pool.insert(5)
    random_pool.delete(2)
    print(random_pool.get_random())
