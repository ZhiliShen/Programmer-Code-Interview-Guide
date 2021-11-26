# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-26 18:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import random
from collections import deque


def rand1to5():  # 等概率生成1~5的
    return int(random.random() * 5) + 1


# 可以利用rand1to5等概率地生成7个不同的数 例如将两个rand1to5相乘 从中选取等概率的7个不同的数
# 但为了尽可能地减少调用rand1to5的次数 我们应该将拒绝采样的次数减少
# rand1to5-1等概率产生0~4 (rand1to5-1)*5等概率产生0,5,10,15,20 则rand1to5-1 + (rand1to5-1)*5等概率产生0~24
# 通过对21~24拒绝采样 并将0~20映射到0~6
# 因为0~20共有21个不同的数 是7的倍数 因此选择0~20
# 实现rand1to7调用rand1to5次数的期望 我们称连续两次调用rand1to5为一轮 第一轮中有21/25的概率被接受 4/25的概率被拒绝因此进入第二轮
# 第二轮中有pow(4/25, 2)的概率被拒绝 因此进入第三轮
# 因此rand1to7调用rand1to5次数的期望为
# 2+2*4/25+2*pow(4/25, 2)+...
# 2*1/(1-4/25)
# 50/21
def rand1to7():
    while True:
        num = (rand1to5() - 1) * 5 + rand1to5() - 1
        if num <= 20:
            return num % 7 + 1


def rand01p(p: float):  # 以p的概率生成0 1-p的概率生成1
    return 0 if random.random() < p else 1


# 利用生成01与10的概率是一致的性质 将01与10分别映射至0与1
def rand0to1():  # 等概率生成0~1
    while True:
        num = rand01p(0.1)
        if num != rand01p(0.1):
            return num


# rand0to1等概率生成0,1
# rand0to1*2等概率生成0,2
# rand0to1 + rand0to1*2等概率生成0~3
def rand0to3():  # 等概率生成0~3
    num = rand0to1() + rand0to1() * 2
    return num


# rand0to3等概率生成0~3
# rand0to3*4等概率生成0,4,8,12
# rand0to3 + rand0to3*4等概率生成0~15
# 通过对12~15拒绝采样 并将0~11映射到0~5
# 通过在其基础上+1 则能等概率生成1~6
def rand1to6():
    while True:
        num = rand0to3() + rand0to3() * 4
        if num <= 11:
            return num % 6 + 1


def rand1tom(m: int):  # 等概率生成1~m
    return int(random.random() * m) + 1


def value2m(value: int, m: int):  # 将value转换为m进制
    queue = deque()
    while value != 0:
        queue.appendleft(value % m)
        value //= m
    return queue


def get_random_m_less_value(queue: deque, m: int):  # 等概率生成0~value
    index = 0
    res = []
    last_equal = True
    while index != len(queue):
        cur_num = rand1tom(m) - 1
        if last_equal:
            if cur_num > queue[index]:  # 如果当前位数生成的随机数超过范围 则进行拒绝 重新生成
                index = 0
                res = []  # 注意将res清空 全部复原
                last_equal = True
                continue
            else:   # 如果当前位数生成的随机数比目标小 则后面生成的随机数一定在合法范围内
                last_equal = (cur_num == queue[index])
        res.append(cur_num)
        index += 1
    return res


def m2value(queue: list, m: int):  # 将m进制的数转换为10进制
    res = 0
    for num in queue:
        res = res * m + num
    return res


def rand1ton(n: int, m: int):
    value_queue = value2m(n - 1, m)  # 注意这里传参是n-1
    random_value = get_random_m_less_value(value_queue, m)
    return m2value(random_value, m) + 1  # 注意这里返回的时候需要+1


if __name__ == "__main__":
    test = []
    for _ in range(10000):
        test.append(rand1ton(10, 2))
    from collections import Counter
    counter = Counter(test)
    print(counter)
