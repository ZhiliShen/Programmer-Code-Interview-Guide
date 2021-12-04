# -*- coding: utf-8 -*- #
# @Time    : 2021-12-03 21:06
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

# [3, 2, 5]
# 首先如果只有3的话 则能组成的为0+3
# 其次如果有3 2的话 则能组成的是0+2=2 3+2=5
# 最后如果有3 2 5的话 则能组成的是0+5=5 3+5=8 2+5=7 5+5=10
# 所以能组成的是上面的并集减去0
def unformed_sum(array: list):
    sum_set = set()
    process(array, 0, 0, sum_set)
    array_min = min(array)
    cur_sum = array_min + 1
    while True:
        if cur_sum not in sum_set:
            return cur_sum
        cur_sum += 1


def process(array: list, index: int, cur_sum: int, sum_set: set):
    if index == len(array):
        sum_set.add(cur_sum)
        return  # 写递归函数一定要return
    process(array, index + 1, cur_sum, sum_set)
    process(array, index + 1, cur_sum + array[index], sum_set)


# 在这个过程中我们是逆着来的 因为原则就是不要在遍历数组的时候改变数组 否则以上述为例 则会出现3变为True 进而将6变为True 而逆序的话则不会出现这样的现象
def unformed_sum_1(array: list):
    array_sum = sum(array)
    array_min = min(array)
    dp = [False for _ in range(array_sum + 1)]
    dp[0] = True
    for i in range(len(array)):
        for j in range(array_sum, array[i] - 1, -1):
            if dp[j - array[i]]:
                dp[j] = True
    for i in range(array_min, array_sum + 1):
        if not dp[i]:
            return i

    return array_sum + 1


def unformed_sum_2(array: list):
    array_sum = sum(array)
    array_min = min(array)
    set_a = set()
    set_a.add(0)
    for i in range(len(array)):
        set_b = set()
        for num in set_a:
            set_b.add(num + array[i])
        set_a = set_a.union(set_b)
    for i in range(array_min, array_sum + 1):
        if i not in set_a:
            return i
    return array_sum + 1


# 1的存在使得范围能够连续起来
def unformed_sum_3(array: list):
    array.sort()
    legal_range = 0
    for num in array:
        if num <= legal_range + 1:
            legal_range += num
        else:
            return legal_range + 1
    return legal_range + 1  # 注意子集和是连续的情况


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    print(unformed_sum_1(test))
