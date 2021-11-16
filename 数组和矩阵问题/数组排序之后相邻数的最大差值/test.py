# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-16 12:33
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def max_gap(array: list):
    if array is None or len(array) < 2:
        return 0
    array_len = len(array)
    array_min, array_max = min(array), max(array)
    # 计算得到数组中的最大数字与最小数字 之后一共会有len(array)+1个桶 每个桶内的数字之差小于(max-min)//len(array) 为什么不是len(array) 是因为最后一个桶里面只会存放最大值
    if array_min == array_max:  # 数组中全部为同一种数字 则不用继续处理
        return 0
    has_num = [False for _ in range(array_len+1)]
    bucket_min = [float('inf') for _ in range(array_len+1)]
    bucket_max = [-float('inf') for _ in range(array_len+1)]

    # base case
    has_num[-1], bucket_min[-1], bucket_max[-1] = True, array_max, array_min

    for num in array:
        # 因为桶内最大值与最小值计算得出最大差值的关键 所以我们只它们
        bucket_id = (num-array_min)*array_len//(array_max-array_min)
        bucket_min[bucket_id] = min(bucket_min[bucket_id], num) if has_num[bucket_id] else num
        bucket_max[bucket_id] = max(bucket_max[bucket_id], num) if has_num[bucket_id] else num
        has_num[bucket_id] = True

    prev_max = bucket_max[0]
    res = 0
    for i in range(1, len(array)+1):  # 第一个桶没必要考虑
        # len(array)个数放进len(array)+1个桶内 则一定有空桶 桶内最大差值小于(max-min)//len(array) 所以最大差值只发生空桶相邻的两个非空桶
        if has_num[i]:
            res = max(res, bucket_min[i]-prev_max)
            prev_max = bucket_max[i]

    return res


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(max_gap(test))
