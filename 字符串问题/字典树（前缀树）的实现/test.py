# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-22 22:18
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
class TrieNode:
    def __init__(self):
        self.path = 0
        self.end = 0
        self.child_nodes = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        if word is None:
            return
        node = self.root
        node.path += 1
        for char in word:
            index = ord(char) - ord('a')
            if node.child_nodes[index] is None:
                node.child_nodes[index] = TrieNode()
            node = node.child_nodes[index]
            node.path += 1
        node.end += 1

    def delete(self, word: str):
        if self.search(word):
            node = self.root
            for char in word:
                index = ord(char) - ord('a')
                node.child_nodes[index].path -= 1
                if node.child_nodes[index].path == 0:
                    node.child_nodes[index] = None
                    return
                node = node.child_nodes[index]
            # 这一步后面不需要再去判断其end是否为0 进而是否需要设置为空 因为path为0时 end也必然为0 所以早在循环中就已经处理 能走出循环就说明有不止一个word
            node.end -= 1

    def search(self, word: str) -> bool:
        if word is None:
            return False
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.child_nodes[index] is None:
                return False
            node = node.child_nodes[index]
        if node.end >= 1:  # 有可能end会大于1 此时也是找到的
            return True
        else:
            return False

    def prefix_number(self, word: str) -> int:
        if word is None:
            return 0
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.child_nodes[index] is None:
                return 0
            node = node.child_nodes[ord(char) - ord('a')]
        return node.path


if __name__ == "__main__":
    n = int(input())
    trie = Trie()
    for _ in range(n):
        op, test = input().split()
        if op == '1':
            trie.insert(test)
        elif op == '2':
            trie.delete(test)
        elif op == '3':
            print('YES' if trie.search(test) else 'NO')
        else:
            print(trie.prefix_number(test))
