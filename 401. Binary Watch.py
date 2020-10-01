class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        numToSetBits={i:bin(i).count('1') for i in range(60)}
        SetBits_Nums=defaultdict(list)
        for i in numToSetBits:
            SetBits_Nums[numToSetBits[i]].append(i)
        
        solution=[]
        
        # selecting the hour
        hour=None
        for sbhour in range(n+1):
            for hour in SetBits_Nums[sbhour]:
                if hour>11:
                    break
                sbminute=n-sbhour
                for minute in SetBits_Nums[sbminute]:
                    peace=''
                    if minute<10:
                        peace='0'
                    solution.append(str(hour)+':'+peace+str(minute))
        return solution
