
# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    answer = []

    stage_info = [[i, 0, 0] for i in range(N + 2)]
    max_stage = 0

    for s in stages:
        stage_info[s][1] += 1
        if s > max_stage:
            max_stage = s
        for clear in range(1, s + 1):
            stage_info[clear][2] += 1

    if max_stage > N:
        # divide by zero 해결을 위함
        max_stage = N

    for_calculate = stage_info[1:max_stage + 1]
    for_calculate.sort(key=lambda x: -x[1] / x[2])
    
    answer = [i[0] for i in for_calculate] + [i for i in range(max_stage+1, N + 1)]

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(5, [4,4,4,4,4]))