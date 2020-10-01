class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Using Greedy Approach
        R=0; L=0
        sol=0
        for i in s:
            if i=='L':
                L+=1
            else:
                R+=1
            if L==R:
                sol+=1
                L=0; R=0
        return sol
