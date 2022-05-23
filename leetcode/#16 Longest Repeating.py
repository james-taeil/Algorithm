def characterReplacement(self, s: str, k: int) -> int:
        max_count, start = 0, 0
        result = 0
        seen = dict()
        
        for i, c in enumerate(s):
            seen[c] = seen.get(c, 0) + 1
            max_count = max(max_count, seen[c])
            
            if i - start + 1 - max_count > k:
                seen[s[start]] -= 1
                start += 1
                
            result = max(result, i - start + 1)
        return result
