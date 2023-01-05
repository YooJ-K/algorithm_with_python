def solution(s):
    answer = True
    
    s = s.lower()

    count = [0, 0]
    for a in s:
        if a == 'p':
            count[0] += 1
        elif a == 'y':
            count[1] += 1

    if count[0] != count[1]:
        answer = False
    
    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))