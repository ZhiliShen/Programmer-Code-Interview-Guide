# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-21 12:28
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def max_unique(array: List[int]):
    array_length = len(array)
    if array_length == 0:
        return 0
    if array_length == 1:
        return 1

    num2pre_pos = {}  # 存储的是每一个字符在当前情况下最近一次出现的位置
    pre = -1  # 代表的是以当前指向的字符的前一个字符为结尾的最长无重复子串的开始位置的前一个位置 eg babcb 若当前指向字符为末尾b 则pre指向为第一个b
    result = 0  # 最终的结果

    # for i in range(array_length):
    #     cur_num_pre_pos = num2pre_pos.get(array[i], None)
    #     if cur_num_pre_pos is not None:  # 如果这个字符出现过
    #         if pre < cur_num_pre_pos:  # 而且其位置在pre的右边 例如 aabcb cur_num_pre_pos=2 pre=0 则pre更新为cur_num_pre_pos
    #             pre = cur_num_pre_pos  # 原因则是因为cur_num_pre_pos与当前指向字符一致 不能包含 而[cur_num_pre_pos+1, i]区间段内原本就属于[pre+1, i-1] 这一段已经证明是无重复子串
    #             result = max(result, i-pre)  # 而且其也不包含i 因为i最近出现的一次位置是在cur_num_pre_pos
    #             num2pre_pos[array[i]] = i
    #         else:  # 如果其位置在pre的左边 例如 baacdb cur_num_pre_pos=0 pre=1 则pre保持不变 直接加入即可
    #             result = max(result, i-pre)  # 因为i最近出现的一次位置在pre的左边 所以[pre+1, i-1]是不会有i的
    #             num2pre_pos[array[i]] = i
    #     else:  # 如果这个字符没出现过 直接加入即可
    #         result = max(result, i-pre)
    #         num2pre_pos[array[i]] = i
    # 有一个很有趣的问题就是pre会不会等于cur_num_pre_pos
    # 答案是不会的
    # 首先假设pre=cur_num_pre_pos
    # 因为pre没有包含进去 说明[pre+1, i-1]这个区间段一定是有pre的 如果没有pre 则不符合最长的定义
    # 则cur_num_pre_pos>pre 与假设相反 所以假设不成立

    # 这段代码就是由上面这段代码优化而来 虽然更短 但是上面的代码可读性更强
    for i in range(array_length):
        cur_num_pre_pos = num2pre_pos.get(array[i], -1)
        pre = max(pre, cur_num_pre_pos)
        result = max(result, i - pre)
        num2pre_pos[array[i]] = i

    return result


if __name__ == "__main__":
    num = int(input())
    test = list(map(int, input().split()))
    print(max_unique(test))
