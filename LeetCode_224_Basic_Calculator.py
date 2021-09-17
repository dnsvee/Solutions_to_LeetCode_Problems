# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        import re
        
        # tokenize
        ts = re.findall(r'(\+|-|\d+|\(|\))', s)

        # convert if possible string to numbers
        def numconverter(n):
            try:
                return int(n)
            except:
                return n
        
        ts = [numconverter(t) for t in ts]
        
        # reverse list for more effiency
        ts.reverse()

        # returns value of sub expression or total expression
        def calc0():
            # special init state; also deals with negative sign
            # issues
            nms = [0]
            ops = ['+']

            while len(ts):
                t = ts.pop()

                # calculate sub expression
                if t == '(':
                    t = calc0()
                    
                # operator found so push to stack
                if t == '+' or t == '-':
                    ops.append(t)
                    
                # number found; triggers evaluation
                elif type(t) == type(1):
                    a = nms.pop()

                    nms.append(a + t if ops.pop() =='+' else a - t)

                # end of sub expression or end of input    
                if t == ')' or len(ts) == 0:
                    break
                    
            # returns value as number
            return nms.pop()
            
        return calc0()
            
