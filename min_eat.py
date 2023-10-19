import math


def min_eat(piles, H):
    def truth(K):
        n = 0
        for p in piles:
            n += p / K
        print(n)
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p / K)
        return total_hours <= H

    start = 1
    end = max(piles)
    while start < end:
        mid = (start + end) // 2
        if not truth(mid):
            start = mid + 1
        else:
            end = mid
    return start


print(min_eat([30, 11, 23, 4, 20], 6))
