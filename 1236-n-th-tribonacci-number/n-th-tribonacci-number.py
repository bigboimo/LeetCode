class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1
        
        #Storing only last 3 sub-problems for most optimal space complexity. T(n) =  T(n-1) + T(n-2) + T(n-3). This recurrence shows we only need last 3 subproblem solutions therefore a hashset is not needed. 
        for i in range(3, n + 1):
            next_trib = a + b + c
            a = b
            b = c
            c = next_trib

        return c