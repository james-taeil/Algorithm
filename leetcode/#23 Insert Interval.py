def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    left, right = 0, 0
    
    while i < len(intervals):
        sn, en = newInterval
        s, e = intervals[left]
        
        if sn > e:
            left += 1
        elif en < s:
            return intervals[:left - right] + [newInterval] + intervals[left:]
        else:
            newInterval = [min(sn, s), max(en, e)]
            left += 1
            right += 1
    return intervals[:left - right] + [newInterval]