
# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix):
        # so the solution goes as follows:
        # first the matrix is turned into a dict with (y, x) as key 
        #  and the value of the cell (visiting order) as value of the dict entry
        # visit each element of the matrix in a spiral fashion 
        #  and add the value of the cell visited to the result list
        # when a cell is visited remove it from the dict
        # set the current point to (0, 0) and add an offset to it on each
        #  iteration to visit the next cell
        # there are four offsets one for moving into each direction
        # lookup the next potential coordinate to visit as the key in the dict 
        # the key is equal to the current coordinate plus the current offset 
        # if it exists visit it and set this coordinate to current coordinate
        # if it does not exist then set the next offset to the current offset 
        #  and try again
        # cycle through the four offsets to create the spiral movement
        # when the dict is empty your done
        
        V = {}
        for y, e in enumerate(matrix):
            for x, v in enumerate(e):
                V[(y, x)] = v
                
        O1, O2, O3, O4 = (1,0), (0,1), (-1,0), (0,-1)

        # starting point is (-1, 0) will be (0, 0) when loop first entered
        x, y = -1, 0

        # result
        R = []

        while len(V):            
            # see if next current coordinate can be reached from current point
            val = V.get((y + O1[1], x + O1[0]))
            
            if val is None:
                # if not then try next offset by cycling through the offsets
                O1, O2, O3, O4 = O2, O3, O4, O1
                continue

            # set new current coordinate
            x, y = x + O1[0], y + O1[1]

            # add value of current point to result array and delete from dict
            del V[(y, x)]
            R.append(val)
            

        return R
