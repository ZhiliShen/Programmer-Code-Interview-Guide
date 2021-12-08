# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-08 14:01
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :


# 分发糖果的规则可以拆分为 当评分[i-1]<评分[i]的时候 则i的糖果要比i-1的要多
# 当评分[i]>评分[i+1]的时候 则i的糖果要比i+1的要多
# 因此可以遍历数组两次 生成出每个学生分别满足第一条规则和第二条规则所需要的最少的糖果 并取其中最大值最为最终值
def candy(array: list):
    left_dp, right_dp = [1 for _ in range(len(array))], [1 for _ in range(len(array))]
    for index in range(1, len(left_dp)):
        if array[index] > array[index-1]:
            left_dp[index] = left_dp[index-1]+1
        else:
            left_dp[index] = 1
    for index in range(len(right_dp)-2, -1, -1):  # 其实在这里就已经可以开始比较left_candy与right_candy之间的大小 从而得出最后的结果
        if array[index] > array[index+1]:
            right_dp[index] = right_dp[index+1]+1
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
    # 以 1 2 5 4 3 2 1举例
    for index in range(1, len(array)):
        if array[index] > array[index-1]:  # 如果当前学生的分数大于左边学生的分数
            pre += 1  # 则当前学生所分得的糖果要比左边的学生多一个
            if dec_len != 0:  # 如果前面的学生是递减序列的一部分 则递增序列的长度需要重新计算 记为2
                inc_len = 2
            else:  # 如果前面的学生是递增序列的一部分 则递增序列的长度+1
                inc_len += 1
            dec_len = 0  # 当前递减序列长度归零
            res += pre
        elif array[index] == array[index-1]:  # 如果当前学生的分数等于左边学生的分数
            dec_len = 0   # 当前递减序列长度归零
            pre = 1
            inc_len = 1
            res += pre
        else:
            # 以1 5 3 2 1为例 遍历到5时 此时分配给5的是2颗 递增序列长度为2 遍历到3时 此时分配给3的是1颗 递增序列长度不变 这也是为什么不在该分支中更改递增序列长度的原因
            # 遍历到2时 此时想分配给2的是一颗 但一旦只给1颗 就小于旁边的3 所以干脆整个递减序列中的元素都增加1颗 所以此时累加的目标变为递减序列长度
            # 但此时还是不满足要求 因为3分得的糖果虽然大于2分得的糖果 但也等于5了 所以5的糖果数量也需要增加 而是否增加的依据就是看递增序列长度与递减序列长度是否相等
            # 一旦相等 则需要将递增序列中的最后一个元素放入递减序列当中
            # 以1 4 4 3 2 1为例 第二个4为2颗 第三个4为1颗 此时遍历到第三个4的时候递增序列长度应当为1 因此遍历到3的时候 就会将第三个4纳入到递减序列当中
            dec_len += 1
            if dec_len == inc_len:
                dec_len += 1
            pre = 1
            res += dec_len
    return res


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    print(candy_1(test))
