def solution(n):
    if n <= 200:
        return str(count(1, n) - 1)
    else:
        return 0
    
    
def count(height, left):
    if left == 0:
        return 1

    if left < height:
        return 0

    return count(height + 1, left - height) + count(height + 1, left)

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(200))
