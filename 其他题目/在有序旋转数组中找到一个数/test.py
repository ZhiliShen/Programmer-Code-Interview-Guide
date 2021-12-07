# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-06 10:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 先找到断点 得到两个有序的数组 在两个有序的数组中进行二分查找 也是最容易理解的写法
def find_break_points(array: list):
    left, right = 0, len(array) - 1  # 注意这里取得是len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < array[right]:
            right = mid
        elif array[mid] > array[left]:
            left = mid + 1
        else:
            if array[right - 1] <= array[right]:
                right -= 1
            else:
                return right
    return left  # 不要忘了这一步！


def binary_search(array: list, target: int, left: int, right: int):
    boundary = right
    # 最后[0, left)中的元素是小于target [right, len(array)-1]中的元素是大于等于target的 [left, right)是待检验元素
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < target:
            left += 1
        else:
            right = mid
    if right < boundary and array[right] == target:
        return right
    else:
        return -1


def binary_search_1(array: list, target: int):
    left, right = 0, len(array)-1
    while left <= right:
        mid = left + (right-left)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

def find_target(array: list, target):
    min_index = find_break_points(array)
    result_a, result_b = binary_search(array, target, 0, min_index), binary_search(array, target, min_index, len(array))
    if result_a == -1 and result_b == -1:
        return False
    else:
        return True


# 更为简洁的写法 但只适用于数组中不存在重复的数 即严格升序 左闭右开
def find_target_1(array: list, target):
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if deal_boundary(array, mid, target):
            right = mid
        else:
            left = mid + 1
    if left < len(array) and array[left] == target:
        return left
    else:
        return -1


# 更为简洁的写法 只适用于数组中不存在重复的数 即严格升序 LEETCODE官方写法
def find_target_3(array: list, target: int):
    left, right = 0, len(array)-1
    while left <= right:
        mid = left + (right-left)//2
        if array[mid] == target:
            return mid
        if array[left] <= array[mid]:
            if array[left] <= target < array[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if array[mid] < target <= array[right]:
                left = mid+1
            else:
                right = mid-1
    return -1


def deal_boundary(array: list, index: int, target: int):
    if array[index] >= array[0]:  # mid在断点左侧
        return array[0] <= target <= array[index]
    else:  # mid在断点右侧
        return array[0] <= target or target <= array[index]


# 更为简洁的写法 适用于数组中存在重复的数 即不降序 左闭右闭 LEETCODE官方写法
def find_target_2(array: list, target: int):
    left, right = 0, len(array)-1
    while left <= right:
        mid = left + (right-left)//2
        if array[mid] == target:
            return True
        if array[left] == array[mid] == array[right]:
            left += 1
            right -= 1
        elif array[left] <= array[mid]:
            if array[left] <= target < array[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if array[mid] < target <= array[right]:
                left = mid+1
            else:
                right = mid-1
    return False


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print('Yes' if find_target(test, b) else 'No')
