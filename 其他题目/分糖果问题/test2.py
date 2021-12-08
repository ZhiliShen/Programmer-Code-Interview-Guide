# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-08 16:34
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :


# 分发糖果的规则可以拆分为 当评分[i-1]<评分[i]的时候 则i的糖果要比i-1的要多
# 当评分[i]>评分[i+1]的时候 则i的糖果要比i+1的要多
# 当评分[i]=评分[i+1]的时候 则i的糖果要与i+1的相等
# 因此可以遍历数组两次 生成出每个学生分别满足第一条规则和第二条规则所需要的最少的糖果 并取其中最大值最为最终值
def candy(array: list):
    left_dp, right_dp = [1 for _ in range(len(array))], [1 for _ in range(len(array))]
    for index in range(1, len(left_dp)):
        if array[index] > array[index-1]:
            left_dp[index] = left_dp[index-1]+1
        elif array[index] == array[index-1]:
            left_dp[index] = left_dp[index - 1]
        else:
            left_dp[index] = 1
    for index in range(len(right_dp)-2, -1, -1):  # 其实在这里就已经可以开始比较left_candy与right_candy之间的大小 从而得出最后的结果
        if array[index] > array[index+1]:
            right_dp[index] = right_dp[index+1]+1
        elif array[index] == array[index-1]:
            right_dp[index] = right_dp[index-1]
        else:
            right_dp[index] = 1
    res = 0
    for left_candy, right_candy in zip(left_dp, right_dp):
        res += max(left_candy, right_candy)
    return res


def candy_1(array: list):
    res = 1
    pre = 1  # 前一个学生分得的糖果数量
    dec_len = 0  # 当前递减序列长度
    inc_len = 1  # 当前递增序列长度
    equal_len = 1  # 当前相同序列长度
    for index in range(1, len(array)):
        if array[index] > array[index-1]:
            pre += 1
            if dec_len != 0:
                inc_len = 2
            else:
                inc_len += 1
            dec_len = 0
            res += pre
            equal_len = 1
        elif array[index] == array[index-1]:
            equal_len += 1
            dec_len = 0
            pre = pre
            inc_len = 1
            res += pre
        else:
            dec_len += 1
            # 以 1 2 4 4 4 3 2 1 为例 当递增序列与递减序列长度相等时候 相同序列中的所有序列都必须要增加1 所以此时累加的目标变为相同序列长度
            if dec_len == inc_len:
                dec_len += equal_len
            pre = 1
            res += dec_len
            equal_len = 1
    return res


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    print(candy_1(test))
