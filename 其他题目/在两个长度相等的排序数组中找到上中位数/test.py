# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-09 20:54
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def get_k_th_num_in_two_arrays(array_a: list, array_b: list, k: int):
    len_a, len_b = len(array_a), len(array_b)
    index_a, index_b = 0, 0
    while True:
        if index_a == len_a:
            return array_b[index_b + k - 1]
        if index_b == len_b:
            return array_a[index_a + k - 1]
        if k == 1:
            return min(array_a[index_a], array_b[index_b])
        cmp_index_a = min(index_a + k // 2 - 1, len_a - 1)
        cmp_index_b = min(index_b + k // 2 - 1, len_b - 1)
        cmp_a, cmp_b = array_a[cmp_index_a], array_b[cmp_index_b]
        if cmp_a <= cmp_b:
            k -= (cmp_index_a - index_a + 1)
            index_a = cmp_index_a + 1
        else:
            k -= (cmp_index_b - index_b + 1)
            index_b = cmp_index_b + 1


#  这道题则利用了两个等长的有序数组中的上中位数具有传递性的特点
def get_up_median(array_a: list, array_b: list):
    start_a, start_b = 0, 0
    end_a, end_b = len(array_a) - 1, len(array_b) - 1
    while start_a < end_a:
        mid_a, mid_b = start_a + (end_a - start_a) // 2, start_b + (end_b - start_b) // 2
        offset = (end_a - start_a + 1) & 1 ^ 1  # 先得出当前数组的长度是奇数还是偶数 如果是奇数 则不偏移 如果是偶数 则偏移
        if array_a[mid_a] > array_b[mid_b]:
            # 1 2 3 4 5
            # a b c d e 如果3>c 则4 5没有希望成为中位数 a b没有希望成为中位数
            # 1 2 3 4
            # a b c d如果2>b 则3 4没有希望成为中位数 a b没有希望成为中位数 所以此时需要偏移
            end_a = mid_a
            start_b = mid_b + offset
        elif array_a[mid_a] < array_b[mid_b]:
            start_a = mid_a + offset
            end_b = mid_b
        else:
            return array_a[mid_a]
    # 如果每个数组的长度为1 则直接返回其中较小的即可
    return min(array_a[start_a], array_b[start_b])


if __name__ == "__main__":
    a = int(input())
    test_1 = list(map(int, input().split()))
    test_2 = list(map(int, input().split()))
    print(get_up_median(test_1, test_2))
