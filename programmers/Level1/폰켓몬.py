def solution(nums):
    answer = 0
    num_of_kind = len(list(set(nums)))
    n_div_2 = len(nums) // 2
    
    if num_of_kind < n_div_2:
        answer = num_of_kind
    else:
        answer = n_div_2
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))