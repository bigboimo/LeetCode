class Solution:
    def isHappy(self, n: int) -> bool:
       
        num = str(n)
        tot = 0
        tracker = set()

        while tot != 1:
            tot = 0
            
            for i in range(len(num)):
                tot += int(num[i])**2

            num = str(tot)

            if num not in tracker:
                tracker.add(num)
            else:
                return False
                

        return True