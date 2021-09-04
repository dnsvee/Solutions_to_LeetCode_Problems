# https://leetcode.com/problems/contains-duplicate-iii/
    
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # make a new list of nums that has the following properties
        # 1. each item is a tuple of (index, value)
        # 2. it's sorted on value
        # create two pointers i & j that start at element 0 and 1
        # advance j when values are in valid range (<=t) otherwise advance i
        # because the list is sorted we can advance i moderately fast
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        i    = 0
        j    = 1
        try:
            while True:
                # check if values in required range
                if abs(nums[j][1] - nums[i][1]) <= t:
                    # if they are check if indices are in required range
                    if abs(nums[j][0] - nums[i][0]) <= k:
                        # if so return True
                        return True
                    j += 1
                else:
                    i += 1
                    j = i + 1
        except:
            return False

