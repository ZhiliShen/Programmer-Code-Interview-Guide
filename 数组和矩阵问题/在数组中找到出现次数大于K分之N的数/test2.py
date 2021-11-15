# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-15 14:07
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :


def print_k_major(array: list, k: int):
    if k < 2:  # 出现次数大于len(array)的数是肯定不存在的 因为数组也才len(array)大
        return -1
    candidates = {}
    res = []
    for num in array:  # 先将候选名单填满
        if candidates.get(num, None) is None:
            if len(candidates) == k - 1:  # 如果该候选人是候选名单最后一位 对候选名单中的候选人进行清理 因为需要对候选人清理1票 而当前候选人只有1票 所以当前候选人也不用添加
                candidates_minus_one(candidates)
            else:  # 如果当前候选名单仍然存在富余 则将当前候选人添加进来
                candidates[num] = 1
        else:  # 候选人有多张选票 则进行计数
            candidates[num] += 1

    candidates_count = check_candidates_legal(array, candidates)  # 计算候选人真正选票
    has_legal_candidates = False
    for key, value in candidates_count.items():
        if value * k > len(array):  # 检查候选人资格
            res.append(key)
            has_legal_candidates = True

    return res if has_legal_candidates else -1


def candidates_minus_one(candidates: dict):
    remove_list = []
    for key, value in candidates.items():  # 不能在字典遍历的时候改变字典的大小
        if value == 1:  # 如果当前候选人只有1票 则清理出当前候选名单
            remove_list.append(key)
        else:
            candidates[key] -= 1
    for candidate in remove_list:
        candidates.pop(candidate)


def check_candidates_legal(array: list, candidates: dict):
    candidates_count = {}
    for num in array:
        if candidates.get(num, None) is not None:
            if candidates_count.get(num, None) is None:
                candidates_count[num] = 1
            else:
                candidates_count[num] += 1
    return candidates_count


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    ans = print_k_major(test, b)
    if ans == -1:
        print(-1)
    else:
        print(*ans)
