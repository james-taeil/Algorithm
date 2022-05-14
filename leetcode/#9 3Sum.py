def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while left < right:
                num_sum = nums[i] + nums[left] + nums[right]
                
                if num_sum > 0:
                    right -= 1
                
                elif num_sum < 0:
                    left += 1
                
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # 중복제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return answer
