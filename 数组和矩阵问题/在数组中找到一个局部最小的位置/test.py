# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-11 11:19
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def binary_search(array: list, target: int):
    low, high = 0, len(array)  # [low, high)
    while low < high:  # [low, high) 其中low==high时 该区间为空 所以low<high
        mid = low + (high - low) // 2
        if array[mid] < target:  # 这个寻找的是第一个大于等于target的元素 [左边, low)<target 此时mid<target low取mid+1 才能将mid囊括进区间内
            low = mid + 1
        else:  # [high, 右边)>=target 此时mid<=target high取mid就已经能把mid囊括进去
            high = mid

    return high


def get_less_index(array: list):
    array_len = len(array)
    if array_len == 0:
        return -1
    if array_len == 1 or array[0] < array[1]:
        return 0
    if array[array_len - 1] < array[array_len - 2]:
        return array_len - 1

    low, high = 1, len(array) - 1
    while low < high:  # 如果进入到该循环中 则说明数组中的第一个元素和最后一个元素都不是局部最小 说明从第一个元素往后是递减趋势 从最后一个元素往前是递减趋势
        mid = low + (high - low) // 2
        if array[mid] > array[mid - 1]:  # 此时中间的元素往前是递减趋势 此前说过第一个元素往后是递减趋势 则在此区间段内必然会出现波谷 则波谷位置为所求位置
            high = mid
        elif array[mid] > array[mid + 1]:  # 此时中间的元素往后是递减趋势 此前说过最后一个元素往前是递减趋势 则在此区间段内必然会出现波谷 则波谷位置为所求位置
            low = mid + 1
        else:
            return mid

    # low, high = 1, len(array)-2  # 这种写法是[low, high]都有可能出现目标 是左闭右闭区间
    # while low < high:  # 在此种表示方法下 low=high虽然跳出了循环 但并不代表此时区间段中不存在元素 所以最后需要额外的return
    #     mid = low + (high - low) // 2
    #     if array[mid] > array[mid - 1]:
    #         high = mid - 1  # 由于是右闭区间 此时mid已经不可能出现目标 所以high取mid-1
    #     elif array[mid] > array[mid + 1]:
    #         low = mid + 1  # 由于是左闭区间 此时mid已经不可能出现目标 所以low取mid+1
    #     else:
    #         return mid
    # return low


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    print(get_less_index(test))
