

def solution(a, b, n):
    answer = 0
    # 20 -> 10 -> 5 -> 2 + 1 -> 1 + 1

    while n >= a:
        answer += (n // a) * b
        n = n // a + n % a
        
    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))