# 약수의 합

# 냅다 1 ~ n 까지 % 해보고 나눠지면 되고, 아니면 안되고 -> 외에 다른 알고리즘이 존재하나?
# N의 약수를 구할 때는, 1부터 N의 제곱근 까지의 수만 0으로 나누어 떨어지는지 확인하면 된다!
import math

def solution(n):
    answer = 0
    n_sqrt = math.sqrt(n)
    check_range = math.ceil(n_sqrt)
    for i in range(1, check_range + 1):
        if n % i == 0 and i <= n // i:
            answer += i
            if i != n // i:
                answer += n // i

    return answer

print(solution(12)) # 28
print(solution(5)) # 6