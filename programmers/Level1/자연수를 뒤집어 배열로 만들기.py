def solution(n):
    answer = [int(m) for m in str(n)]
    answer.reverse()
    return answer

print(solution(12345))