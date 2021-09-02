#
# https://leetcode.com/problems/trapping-rain-water/
#

class Solution:
    def trap(self, height: List[int]) -> int:
        H = height
        
        left  = [0] * len(H)
        right = [0] * len(H)
        
        # iterate over each bar. For each bar maintain the maximum height
        # of all bars to the left
        m = 0
        for i in range(0, len(H) - 1):
            # m is maximum of all bars
            left[i] = m
            
            # is this bar higher?
            m = max(m, H[i])
            
                
        # iterate over each bar. For each bar maintain the maximum height
        # of all bars to the right
        m = 0
        for i in range(len(H) - 1, -1, -1):
            right[i] = m
            
            # is this bar higher?
            m = max(m, H[i])
            
        sumofall = 0
        for i in range(0, len(H)):
            minh = min(left[i], right[i])
            sumofall += max(0, minh - H[i])           
            
        return sumofall
