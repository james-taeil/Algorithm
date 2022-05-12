from typing import List
def maxProduct(nums:List[int]) -> int:
    max_subarray = max_num = min_num = nums[0]
    
    for num in nums[1:]:
        max_num, min_num = max(num, max_num * num, min_num * num), min(num, max_num * num, min_num * num)
        max_subarray = max(max_num, max_subarray)
    
    return max_subarray