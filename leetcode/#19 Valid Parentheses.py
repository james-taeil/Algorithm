def isValid(self, s: str) -> bool:
        answer = []
        barckets = {')':'(', '}': '{', ']': '['}
        
        for barcket in s:
            # open barcket
            if barcket in barckets.values():
                answer.append(barcket)
            # close barcket
            else:
                if answer and barckets[barcket] == answer[-1]:
                    answer.pop()
                else:
                    return False
        if answer:
            return False
        return True
