#
# https://leetcode.com/problems/integer-to-roman/
#
class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        
        # so when num == 1234 d0 = 4, d1 = 3, d2 = 2, d3 = 1
        
        num, d0 = divmod(num, 10)
        num, d1 = divmod(num, 10)
        num, d2 = divmod(num, 10)
        num, d3 = divmod(num, 10)
        
        # so the idea is to first check if the number has a special form like IV for 4 or IX for 9
        # if not convert digit to roman numeral by using as many numerals to represent
        # the digit so 3 == III, 7 == IIIIIII; but if the number is greater than 5 you can replace 
        # five of the numerals by a V
        # this works for the other type of numerals too

        if   d0 == 4:
            res += ["IV"]
        elif d0 == 9:
            res += ["IX"]
        else:
            b = ['']
            if d0 >= 5:
                b = ['V']
                d0 -= 5
                
            res += ["I"] * d0
            res += b

        if d1   == 4:
            res += ["XL"]
        elif d1 == 9:
            res += ["XC"]
        else:
            b =[""]
            if d1 >= 5:
                b = ["L"]
                d1 -= 5
                
            res += ["X"] * d1
            res += b

        if d2   == 4:
            res += ["CD"]
        elif d2 == 9:
            res += ["CM"]
        else:
            b = [""]
            if d2 >= 5:
                b = ["D"]
                d2 -= 5
                
            res += ["C"] * d2
            res += b
            
        # last trick
        res += ["M"] * d3
            
        # convert and return
        return ''.join(reversed(res))
            