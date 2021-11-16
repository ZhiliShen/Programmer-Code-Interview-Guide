# -*- coding: utf-8 -*- #
# @Time    : 2021-11-15 15:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

def get_max_length_1(array: list, k: int):
    aux_array = [0 for _ in range(len(array) + 1)]
    cur_sum = 0
    for index, num in enumerate(array):
        cur_sum += num
        # [3, -2, 3] -> [3, 1, 4] -> [3, 3, 4] aux存在的意思是为了找到第一个大于等于目标的索引位置 这样才能保证小于等于目标的子数组尽可能长
        aux_array[index + 1] = max(aux_array[index], cur_sum)  # 这里需要确保aux是不降序的 才能使用二分查找

    res = 0
    temp_sum = 0
    for index, num in enumerate(array):
        temp_sum += num
        start_index = binary_search(aux_array, temp_sum - k)  # 这里填的是辅助数组
        res = max(res, index - start_index + 1)  # 不用担心找不到 找不到会返回len(array) 最终结果是负数 超出index范围也是同理 所以不会影响最终结果

    return res


def binary_search(array: list, target: int):
    left, right = 0, len(array)  # [0, left)<target [right, len(array)-1]>=target [left, right) 未确定
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


def get_max_length_2(array: list, k: int):
    min_sums = [0 for _ in range(len(array))]  # 以i开头的元素的子数组的最小累加和
    min_sum_ends = [0 for _ in range(len(array))]  # 以i开头的元素的最小累加和的子数组的右边界

    # base case
    min_sums[-1] = array[-1]
    min_sum_ends[-1] = len(array) - 1

    # transfer equation
    for i in range(len(array) - 2, -1, -1):
        if min_sums[i + 1] <= 0:  # 取小于等于是为了尽可能地扩充子数组长度
            min_sums[i] = array[i] + min_sums[i + 1]
            min_sum_ends[i] = min_sum_ends[i + 1]
        else:
            min_sums[i] = array[i]
            min_sum_ends[i] = i

    left, right_next, cur_sum, res = 0, 0, 0, 0  # [left, right_next)是左闭右开区间段 所以right_next是窗口最右位置的下一个位置 所以初始化为0
    while left < len(array) and right_next < len(array):  # 如果right_next到达了数组的最右边 那么直接后面也不可能有更长的了 因为left往右走只会缩短窗口大小
        # 在整个循环中right_next是不会回退的
        # 假如此时left为5 right_next为10 当开始处理left为6的时候 是没必要将right_next进行回退的 因为我们关注的是最长 回退后算出来的值也不一定大于当前值 所以直接不回退就可以了
        while right_next < len(array) and cur_sum + min_sums[right_next] <= k:  # 如果下一个位置加进来还是满足条件 则进行更新
            cur_sum += min_sums[right_next]
            right_next = min_sum_ends[right_next]+1  # 注意right_next的更新依赖于min_sum_ends
        res = max(res, right_next - left)
        if right_next - left <= 0:
            # right_next += 1
            right_next = left+1  # 如果窗口内不存在数 则直接left, right都需要更新
        else:
            cur_sum -= array[left]  # 如果窗口内存在数 则重新计算当前和
        left += 1

    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print(get_max_length_2(test, b))
