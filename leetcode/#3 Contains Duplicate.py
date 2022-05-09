def containsDuplicate(nums) -> bool:
    nums.sort()
    size = len(nums)
    
    for i in range(1, size):
        if nums[i - 1] == nums[i]:
          return True
    return False
  
print(containsDuplicate(nums=[1, 2, 3, 1]))