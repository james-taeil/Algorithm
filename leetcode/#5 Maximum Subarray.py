from typing import List

def maxSubArray(nums:List[int]) -> int:
    current_subarray, max_subarray = nums[0], nums[0]
    
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
        
    return max_subarray