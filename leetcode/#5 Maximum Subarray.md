## Problems

53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

### 문제
nums 배열에 1개 이상의 정수가 들어온다.
배열 원소들의 연속되는 Subarray 합이 최대가 되는 값을 찾아 return을 하면 된다.

## 카데인 알고리즘
[카데인 알고리즘](https://sustainable-dev.tistory.com/23)

문제를 푸는 방식은 Brute Force 방식과 카데인 알고리즘을 활용하는 방식이다.
O(n^2)이 BF 시간 복잡도라면 카데인 알고리즘은 O(N)으로 성능적으로 굉장히 좋다.

카데인 알고리즘의 핵심 원리는 배열이 한번 도는 동안 최대값을 갱신하는 방법이다.

> MAX A[i] = A[i] vs A[i] + A[i - 1]

## Referance
코드적으로 어려운 부분은 없다. 다만 패턴을 찾아 DP 같은 점화식 개념을 찾는 것이 핵심이다.
```py
from typing import List

def maxSubArray(nums:List[int]) -> int:
    current_subarray, max_subarray = nums[0], nums[0]
    
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
        
    return max_subarray
```

Runtime: 818 ms
Memory Usage: 27.8 MB