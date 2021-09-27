from typing import List


def dynamic_programming(array: List[int]):
    length = len(array)

    # base case
    max_position, num_jump, next_max_position = 0, 0, 0

    # transfer equation
    for i in range(0, length):
        if i > max_position:  # 当max_position无法覆盖当前位置时 则需要扩展到next_max_position 而且next_max_position一定能够覆盖到 所以步数需要增加
            num_jump += 1
            max_position = next_max_position
        next_max_position = max(next_max_position, i+array[i])  # next_max_position表示的是在走num_jump情况下所覆盖的范围再跳一步 所能到达的最远位置

    return num_jump


if __name__ == "__main__":
    n = int(input())
    arr = [int(k) for k in input().split(' ')]
    print(dynamic_programming(arr))
