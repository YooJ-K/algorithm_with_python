def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i + 1))
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))