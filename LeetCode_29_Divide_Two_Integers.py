# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0): 
            sign = -1

        divisor  = abs(divisor )
        dividend = abs(dividend)

        # imagine dividend == 113 and divisor == 17
        # call stack of dbl(17, 1):
        # dbl(17, 1)
        #   dbl(34, 2)
        #     dbl(68, 4)
        #       return sum = 0 + 68 && count = 4
        #     return sum = 68 + 34 == 102 && count = 4 + 2 == 6
        # since 102 + 17 > 113 sum remains 102
        # return count == 6 as result which means floor(113 / 6) == 17
        
        def dbl(num, cnt):
            if num > dividend:
                return 0, 0
            
            s, c = dbl(num + num, cnt + cnt)
            
            if s + num <= dividend:
                s += num
                c += cnt
                
            return s, c

        dividend = abs(dividend)
        divisor  = abs(divisor)
                
        # do the work
        _, res = dbl(divisor, 1)
        
        # fix sign
        res = res if sign == 1 else -res
        
        # clamp result
        mx = ( 1 << 31) - 1 
        mn = (-1 << 31) + 1
        
        if res > 1 << 31 - 1: 
            return (1 << 31) - 1
        
        if res < -1 << 31: 
            return (-1 << 31) + 1
        
        return res
 