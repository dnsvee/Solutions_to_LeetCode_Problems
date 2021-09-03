
# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x : x)
            
            # init state            
            res = [intervals[0]]
            for i in range(1, len(intervals)):  
                # there's a gap between end of previous and start of current so append interval
                # without merging
                # ex [[1,2], [3,4]] => [[1,2], [3,4]]
                if res[-1][1] < intervals[i][0]:
                    res.append(intervals[i])
                    continue

                # there's an overlap so merge
                if res[-1][1] < intervals[i][1]:
                    # ex. [[1,3], [2,4]] => [[1,4]]
                    res[-1][1] = intervals[i][1]
                
            return res
