# Test 1, 3, 5, 9 failed
def solution(n):
    def count_stairs(height, left):
        if left == 0:
            return 1

        if left < height:
            return 0

        return count_stairs(height + 1, left - height) + count_stairs(height + 1, left)
    if n <= 200:
        return str(count_stairs(1, n) - 1)
    else:
        return 0

print(solution(3))
print(solution(4))
print(solution(5))

#print(solution(200))
