## Problems

217. Contains Duplicate
Easy

4591

953

Add to List

Share
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


## 문제 이해
굉장히 쉬운 문제다.
배열안에 중복되는 숫자가 있으면 True없으면 False를 return하면 되는 문제
O(n^2) 말고 N으로 해결을 쉽게 할 수 있다.

1. 반복문으로 배열 한바퀴를 돈다
2. 현재 index와 전 index를 확인하여 값이 같은면 True


## My Solved
```py
def containsDuplicate(nums) -> bool:
    nums.sort()
    size = len(nums)
    
    for i in range(1, size):
        if nums[i - 1] == nums[i]:
          return True
    return False
```
딱 생각대로 한 코드

## Referance or Learn

```py
from collections import Counter

def containsDuplicate(self, nums: List[int]) -> bool:
    coun = Counter(nums)
    for i in coun:
        if coun[i] >=2:
            return True 
    return False
```
신기한 코드를 찾아봤다. Counter이라는 모듈을 사용하여 쉽게 풀 수 있다는 것을 알 수 있었다.

&nbsp;

### #2
```py
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

맞는 풀이방식인지 모르겠지만 중복 숫자 찾는 것에서 set()을 사용하는 방법도 좋은 방법이다.


### #3
```py
def containsDuplicate(self, nums: List[int]) -> bool:
    freq = {}
    for i in nums:
        if freq.get(i): 
            return True
        else: 
            freq[i] = 1
    return False
```

hash를 사용하여 get() 메소드로 해겷하는 방법이다. 이건 생각지도 못했다.