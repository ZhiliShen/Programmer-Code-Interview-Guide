# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-14 19:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
from typing import List


def rotate(array: List[int], left: int, mid: int, right: int):
    reverse(array, left, mid)
    reverse(array, mid+1, right)
    reverse(array, left, right)


def reverse(array: List[int], left: int, right: int):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


def modify_index(index: int, length: int):  # 映射函数 数组以0开头 可以得出在原数组index的在新数组中的位置
    if index < length // 2:
        new_index = 2 * index + 1
    else:
        new_index = 2 * index - length

    return new_index


def cycle_push(array: List[int], left: int, start_index: int, length: int):  # 像多米诺骨牌一样 不断的往前推 理论证明其最终一定是形成一个闭环
    temp = array[start_index]
    next_index = modify_index(start_index-left, length) + left  # 注意modify_index函数是以0开头的 所以要在传参前计算相对位置 计算完后得到绝对位置
    while next_index != start_index:
        array[next_index], temp = temp, array[next_index]
        next_index = modify_index(next_index-left, length) + left
    array[start_index] = temp


def shuffle(array: List[str], n: int):
    if n == 0 or n % 2 != 0:
        return
    # 需要将array拆分成多个3^k-1数组 之后每个3^k-1个数组又会存在1-1 3-1 9-1 3^(k-1)-1共k个起始点
    left, right = 0, n - 1

    while right - left + 1 > 0:  # right-left+1事实上就是size
        n = right - left + 1  # 记住length是要实时更新的
        base = 1
        while pow(3, base) - 1 <= n:
            base += 1
        # 0123456789
        # 12345abcde->1234abcd5e->a1b2c3d45e
        # 123abc->12ab3c->a1b23c
        base -= 1  # 能跳出while循环则必定过界 所以需要倒退
        cur_deal_length = pow(3, base) - 1
        half_cur_deal_length = cur_deal_length // 2
        mid_index = (left+right)//2  # 1234 5 abcd e left后面的half_cur_deal_length是不用的动的 所以left设为left+half_cur_deal_length mid_index后面的half_cur_deal_length是需要翻转过来的 所以right设为mid_index+half_cur_deal_length 那么自然是以原数组的中间位置为枢纽进行交换
        rotate(array, left+half_cur_deal_length, mid_index, mid_index+half_cur_deal_length)  # 选用更为直观的rotate(left, mid, right)
        for k in range(1, base+1):
            index = left + pow(3, k-1)-1
            cycle_push(array, left, index, cur_deal_length)
        left += cur_deal_length

    return array


if __name__ == "__main__":
    num = int(input())
    test = input().split()
    print(' '.join(shuffle(test, num)))
