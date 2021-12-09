# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-09 21:10
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

# 这是我最喜欢的解法 复杂度为O(log(m+n))
# 如果想找第k大的数 则先定位a[k//2-1]与b[k//2-1] 之后比较 其中较小者 前面一定有k//2-1个数 因此最小值在合并后的整体数组中最多是第k//2-1大的数
# 因此可以直接将较小者中所在的数组的[0, k//2-1]删除掉 在剩下的部分中寻找第(k-排除掉个的个数)大的数
def get_k_th_num_in_two_arrays(array_a: list, array_b: list, k: int):
    len_a, len_b = len(array_a), len(array_b)
    index_a, index_b = 0, 0
    while True:
        if index_a == len_a:  # 如果其中一个数组中走到边界 这是最好的情况 这样可以直接在另外一个数组中寻找相应的第k大的数
            return array_b[index_b+k-1]
        if index_b == len_b:
            return array_a[index_a+k-1]
        if k == 1:  # 如果只是寻找第一大的数 由于其有序 则直接返回其中较小的即可
            return min(array_a[index_a], array_b[index_b])
        cmp_index_a = min(index_a+k//2-1, len_a-1)  # 如果其中某个长度不够 则直接选定末尾元素即可
        cmp_index_b = min(index_b+k//2-1, len_b-1)
        cmp_a, cmp_b = array_a[cmp_index_a], array_b[cmp_index_b]
        if cmp_a <= cmp_b:
            k -= (cmp_index_a-index_a+1)  # 在新的剩余部分中 所寻找的第k大的数要根据排除掉的数目进行改变
            index_a = cmp_index_a+1
        else:
            k -= (cmp_index_b-index_b+1)
            index_b = cmp_index_b+1


#  这道题则利用了两个等长的有序数组中的上中位数具有传递性的特点
def get_up_median(array_a: list, array_b: list, start_a: int, end_a: int, start_b: int, end_b: int):
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


# 复杂度为O(log(min(m, n))) 目的就是尽可能将目标数字锁定为两个等长数组的中位数 进而调用在两个长度相等的排序数组中找到上中位数方法
def get_k_th_num_in_two_arrays_1(array_a: list, array_b: list, k: int):
    len_a, len_b = len(array_a), len(array_b)
    if len_a <= len_b:
        array_b, array_a = array_a, array_b
    len_a, len_b = len(array_a), len(array_b)
    if k <= len_a:
        return get_up_median(array_a, array_b, 0, k-1, 0, k-1)
    if k > len_b:
        if array_a[k-len_b-1] >= array_b[len_b-1]:
            return array_a[k-len_b-1]
        if array_b[k-len_a-1] >= array_a[len_a-1]:
            return array_b[k-len_a-1]
        return get_up_median(array_a, array_b, k-len_b, len_a-1, k-len_a, len_b-1)
    if array_b[k-len_a-1] >= array_a[len_a-1]:
        return array_b[k-len_a-1]
    return get_up_median(array_a, array_b, 0, len_a-1, k-len_a, len_b-1)


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    test_1 = list(map(int, input().split()))
    test_2 = list(map(int, input().split()))
    print(get_k_th_num_in_two_arrays_1(test_1, test_2, c))
