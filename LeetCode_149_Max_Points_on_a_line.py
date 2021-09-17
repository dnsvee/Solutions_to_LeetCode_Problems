# 149. Max Points on a Line
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        import math
        
        # sort so points ordered top-to-bottom, left-to-right
        points = sorted(points, key=lambda x : (-x[1], -x[0]))
        
        # for each point calculate the angle with every other point 
        # for each unique angle per point count how many other points have the 
		# same angle compared to point p
        # keep track of the highest number
        # the return values is this number + 1

        tmpmax = 0
        while len(points):
            p = points.pop()
            
            l = dict()
            for p0 in points:
                m = math.atan2(p0[0] - p[0], p0[1] - p[1])
                l[m] = l.get(m, 0) + 1
                tmpmax = max(tmpmax, l[m])
        
        return tmpmax + 1 
