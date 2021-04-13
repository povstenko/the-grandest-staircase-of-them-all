from functools import reduce

def solution(n):
    cache = {}
    
    def count_stairs(start, left):
        if (start, left) not in cache:
            if left == 0:
                cache[(start, left)] = 1
            elif left <= start:
                cache[(start, left)] = 0
            else:
                cache[(start, left)] = reduce(lambda x, item: x + count_stairs(item, left - item), range(start + 1, left + 1), 0)

        return cache[(start, left)]
    
    return count_stairs(0, n) - 1

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(200))