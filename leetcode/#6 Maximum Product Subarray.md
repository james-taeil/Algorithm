## Problems
152. Maximum Product Subarray
Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

> 인접한 원소들과 곱샘을 했을 때, 가장 큰 결과값을 반환

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


## Solved
```py
def maxProduct(nums:List[int]) -> int:
    max_subarray = max_num = min_num = nums[0]
    
    for num in nums[1:]:
        max_num, min_num = max(num, max_num * num, min_num * num), min(num, max_num * num, min_num * num)
        max_subarray = max(max_num, max_subarray)
    
    return max_subarray
```

최대값과 최소값을 활용하는 방법이다. 
일반적인 n^2으로 풀면 시간초과가 난다.

음수 * 음수가 최대값인 경우의 수를 포함해 결과값을 비교하기 위해 지금까지 곱셈의 결과값 중 가장 최소인 결과값과 최대인 결과값을 다음 원소와 곱해나가면서 최대 결과값을 구하면 된다.

```py

max_num, min_num = max(num, max_num * num, min_num * num), min(num, max_num * num, min_num * num)
# Accepted	81 ms	14.3 MB	python3

max_num = max(num, max_num * num, min_num * num)
min_num = min(num, max_num * num, min_num * num)
# 05/12/2022 21:02	Wrong Answer	N/A	N/A	python3
```

위 코드에서 위와 아래는 다르게 결과가 나온다.
무슨 차이인지 잘 모르겠다.


```py
tmp = max_num
max_num = max(num, max_num * num, min_num * num)
min_num = min(num, tmp * num, min_num * num)
```

`tmp = max_num`을 사용해야 코드가 돌아간다. 짐작컨데 min_num은 max_num이 갱신 후라 값이 달라지는 것 같다.
즉, a, b = max(), min()은 스왑이라고 생각하면 될 것 같다.

스왑은 내부 스택에서 별로도 진행되서 max_num이 바뀌지 않는 것 같다.