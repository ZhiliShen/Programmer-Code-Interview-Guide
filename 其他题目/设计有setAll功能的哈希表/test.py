# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-29 22:01
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


class MyHashMap:
    def __init__(self):
        self.hash_map = {}
        self.time = 0
        self.set_all_record = (None, -1)

    def put(self, key, value):
        self.time += 1
        self.hash_map[key] = (value, self.time)

    def set_all(self, value):
        self.time += 1
        self.set_all_record = (value, self.time)

    def get(self, key):
        flag = self.hash_map.get(key, None)
        if flag is not None:
            if flag[-1] > self.set_all_record[-1]:  # 如果该记录的时间戳大于set_all_record 则直接返回
                return flag[0]
            else:  # 如果该记录的时间戳小于set_all_record 则直接返回set_all_record的值 并没有真正的改写相应的值 而是使用了时间换空间的方法
                return self.set_all_record[0]
        else:
            return None


if __name__ == "__main__":
    my_hash_map = MyHashMap()
    a = int(input())
    for _ in range(a):
        a, *b = map(int, input().split())
        if a == 1:
            my_hash_map.put(b[0], b[-1])
        elif a == 2:
            print('-1' if my_hash_map.get(b[0]) is None else my_hash_map.get(b[0]))
        else:
            my_hash_map.set_all(b[0])
