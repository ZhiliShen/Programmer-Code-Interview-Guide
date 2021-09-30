# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-30 09:49
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


class Envelope:
    def __init__(self, length, width):
        self.length = length
        self.width = width


def envelopes2array(envelopes: List[Envelope]):
    arr = []
    for envelope in envelopes:
        arr.append(envelope.width)

    return arr


def binary_search(arr: List[int], left, right, target):
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


def generate_lis_length(nums: List[int]):
    if len(nums) == 0:
        return 0

    ends = [None for i in range(len(nums))]

    # base case
    ends[0] = nums[0]
    ends_points = 0

    # transfer equation
    for num in nums:
        index = binary_search(ends, 0, ends_points + 1, num)
        if index == ends_points + 1:
            ends_points += 1
            ends[ends_points] = num
        else:
            ends[index] = num

    return ends_points + 1


if __name__ == "__main__":
    n = int(input())
    envelopes_list = []

    for i in range(n):
        temp_length, temp_width = map(int, input().split(" "))
        temp_envelope = Envelope(temp_length, temp_width)
        envelopes_list.append(temp_envelope)
    envelopes_list.sort(key=lambda envelope: envelope.width, reverse=True)
    envelopes_list.sort(key=lambda envelope: envelope.length)

    print(generate_lis_length(envelopes2array(envelopes_list)))
