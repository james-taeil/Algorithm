def countBits(self, n: int) -> List[int]:
        answer = []
        
        for el in range(n + 1):
            count = 0
            while el:
                el &= el - 1
                count += 1
            answer.append(count)
        return answer
