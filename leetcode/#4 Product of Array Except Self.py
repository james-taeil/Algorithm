def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    
    tmp = 1
    size = len(nums)
    # left
    for i in range(size):
        answer.append(tmp)
        tmp *= nums[i]
    
    # rigth
    tmp = 1
    for i in range(size-1, -1, -1):
        answer[i] *= tmp
        tmp *= nums[i]
        
    return answer