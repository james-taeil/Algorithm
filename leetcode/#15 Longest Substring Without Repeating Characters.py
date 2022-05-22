def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, max_len = 0, 0, 0
        
        exists = dict()
        
        for idx, char in enumerate(s):
            if char in exists and start <= exists[char]:
                start = exists[char] + 1
            else:
                max_len = max(max_len, idx - start + 1)
            
            exists[char] = idx
            
        return max_len
