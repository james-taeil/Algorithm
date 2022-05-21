def missingNumber(self, nums: List[int]) -> int:
        answer = max(nums)
        cur_nums = set([i for i in range(len(nums) + 1)])
        nums = set(nums)
        
        dif = cur_nums - nums
        
        if dir == 0:
            return answer + 1
        else:
            return list(dif)[0]
