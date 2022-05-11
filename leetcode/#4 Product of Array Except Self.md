## Problem
238 Product of Array Except Self
Medium

12160

740

Add to List

Share
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


## My solved

어떻게든 풀어보려고 했는데, 아이디어가 떠오르지 않았다. 거의 내가 하는 풀이는 O(N^2) 이어서 시간초과가 계속났다.

## Referance
```py
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
```

뭔가 깨닫게 되는 풀이었다. 오른쪽 왼쪽 배열을 한번씩 순회하기 때문에 O(N)으로 시간복잡도는 해결되었다.
아이디어를 보자면 왼쪽 오른쪽 도는 것을 따로 생각한 것이 컸던 것 같다.
