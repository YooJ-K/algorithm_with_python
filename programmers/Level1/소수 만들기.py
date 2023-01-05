def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    nums_len = len(nums)

    for i in range(nums_len):
        for j in range(i + 1, nums_len):
            for k in range(j + 1, nums_len):
                sum_of_3_num = nums[i] + nums[j] + nums[k]
                if isPrime(sum_of_3_num):
                    answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))