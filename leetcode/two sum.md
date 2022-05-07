## Brute Force

```py
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1 , len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

## Two pass Hash Table

```py
def twoSum(self, nums: List[int], target: int) -> List[int]:
    talbe = {num: i for i, num in enumerate(nums)}

    for idx, num in enumerate(nums):
        if ((target - num) in table) and (idx != table[(target - num)]):
            return [idx, table[(target - num)]]
```

## One pass Hash Table

```py
def twoSum(self, nums: List[int], target: int) -> List[int]:
    table = {}

    for idx, num in enumerate(nums):
        complement = target - num

        if complement in talbe:
            return [i, talbe[complement]]
        else:
            talbe[num] = i
```