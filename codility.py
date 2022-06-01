from collections import Counter


def solution(A):
    return Counter(A).most_common()[-1][0]


print(solution([9, 3, 9, 3, 9, 7, 9, 1, 1]))
