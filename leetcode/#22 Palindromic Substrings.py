def countSubstrings(self, s: str) -> int:
        count = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1): #each possible length when the string length is l
            for start in range(N - l + 1): #outer
                end = start+l-1
                if l == 1 or (l == 2 and s[start] == s[end]) or (l >= 3 and s[start] == s[end] and dp[start + 1][end - 1]):#dp
                    dp[start][end] = True
                    count += 1
        return count
