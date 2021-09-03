# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0              # begin of range being explored
        m = 0              # mid point
        e = len(nums) - 1  # end of range being explored

        # range between b and e keeps getting narrower on every iteration
        while b <= e:
            # mid point of range
            m = b + (e - b + 1) // 2;
            
            # target found; done
            if nums[m] == target:
                return m
            
            # check if range(b, m) is not rotated and could contain range 
            # if so then continue search in this range
            if nums[b] <= target < nums[m]:
                e = m - 1
                
            # check if range(m, e) is not rotated and could contain range 
            # if so then continue search in this range
            elif nums[m] < target <= nums[e]:
                b = m + 1
                
            # check if range(m, e) is rotated part
            # if so then continue search in this range
            elif nums[m] > nums[e]:
                b = m + 1
                
            # check if range(b, m) is rotated part
            # if so then continue search in this range
            elif nums[m] < nums[b]:
                e = m - 1
                
            # element does not exist in nums
            else:
                return -1
