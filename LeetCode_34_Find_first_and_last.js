// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
var searchRange = function(nums, target) {
    let l0 = 0, r0 = nums.length - 1, l1 = 0, r1 = nums.length - 1;
    
    let m0, m1;
    
    while (l0 < r0 || l1 < r1) {
           m0 = l0 + Math.floor((r0 - l0    ) / 2);
           m1 = l1 + Math.floor((r1 - l1 + 1) / 2);
        
           if (nums[m0] < target) {
               l0 = m0 + 1;
           } else if (nums[m0] == target) {
               r0 = m0;
           } else {
               r0 = m0 - 1;
           }
        
           if (nums[m1] > target) {
               r1 = m1 - 1;
           } else if (nums[m1] == target) {
               l1 = m1;
           } else {
               l1 = m1 + 1;
           }
    }
    if (nums[r0] == target && nums[l1] == target) return [r0, l1];
    return [-1, -1]
};
