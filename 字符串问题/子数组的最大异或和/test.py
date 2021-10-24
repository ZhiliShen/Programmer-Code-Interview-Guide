# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-23 12:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


# ^: 只要是同一批数字 不论异或顺序如何 最终得到的结果都是一致的
#    a^b=c->a=b^c|b=c^a 该条性质帮助我们不借助第三方变量交换两个变量 a=a^b b=a^b a=a^b 即可交换两个变量
#    0和任何数字异或的结果均为该数字本身 任何数字和自己异或的结果均为0
# 根据以上性质可以推的[i,j]区间段的异或和为[0,j]区间段的异或和异或上[0,i-1]区间段的异或和
# 所以第一个方法即是挨个尝试以j结尾的数组的所有异或和 并找到其中最大的
def max_xor_subarray_1(array: List[int]):
    array_len = len(array)
    if array_len == 0:
        return 0

    eor = [0 for _ in range(array_len)]
    eor[0] = array[0]
    for i in range(1, len(eor)):
        eor[i] = eor[i - 1] ^ array[i]

    result = -float('inf')
    for i in range(0, array_len):
        for j in range(0, i + 1):
            result = max(result, eor[i] if j == 0 else eor[i] ^ eor[j - 1])

    return result


class TrieNode:
    def __init__(self):
        self.child_nodes = [None for _ in range(2)]
        self.num = None


# 但是寻找能凑成最大异或和的另一个区间段并不是没有规律 可以将其存入一个前缀树
# 不同得1 所以选择得时候为了尽可能大 要选择不同的数字
# 但是需要注意的是 最高位是符号位 所以这个时候是不希望得到1的 换句话说 原来符号位是0 则选择1 原来符号位是1 则选择0 进而能得到0 保证是正数
# 但是写这个题的时候 我在想 如果原来符号位是1 现在符号位上只有0可选 而后面的逻辑是越大越好 但符号位是负数的存在 反而使得其得到是较小的数字
# 后来我明白 -3 1 111101 -4 111100 最后一位-3比-4大 结果也正是-3比-4大 原因就在于计算机中存储的是补码 补码是要反码+1的 所以正数的规律仍然适用于负数
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        node = self.root
        for i in range(31, -1, -1):
            index = ((num >> i) & 1)
            if node.child_nodes[index] is None:
                node.child_nodes[index] = TrieNode()
            node = node.child_nodes[index]
        node.num = num

    def max_xor(self, num: int):
        node = self.root
        for i in range(31, -1, -1):
            path = (num >> i) & 1
            choice = path if i == 31 else (path ^ 1)
            choice = choice if node.child_nodes[choice] is not None else (choice ^ 1)  # 先选最好的 没有的话再选有的 而且在任何一个节点都有路可走
            # 这里本来result的获取是result |= (path^choice)<<i
            # 但这样的解法是不适用于python的 因为python存储int时 是符号位+原码形式的 一堆01是只能变成正数的
            # 最简单直观的例子是 1<<31 在python中是2147483648而java是-2147483648 因为在java中这个1被移到了符号位 而python中则不用特定位置来表示符号位
            node = node.child_nodes[choice]
        return num ^ node.num


def max_xor_subarray_2(array: List[int]):
    array_len = len(array)
    if array_len == 0:
        return 0

    result = -float('inf')
    eor = 0
    trie = Trie()
    trie.insert(0)
    for i in range(array_len):
        eor ^= array[i]
        result = max(result, trie.max_xor(eor))
        trie.insert(eor)

    return result


if __name__ == "__main__":
    n = int(input())
    test = []
    for _ in range(n):
        test.append(int(input()))
    print(max_xor_subarray_2(test))
