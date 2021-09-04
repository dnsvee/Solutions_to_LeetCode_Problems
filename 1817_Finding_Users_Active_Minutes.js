/*
https://leetcode.com/problems/finding-the-users-active-minutes/
*/
var findingUsersActiveMinutes = function(logs, k) {
        let Ans = new Array(k).fill(0);
        let D = new Map();
    
        // for each user create a set and add all minutes
        // they were active
        for (const [k, v] of logs) {
            D.set(k, (D.get(k) || new Set()).add(v))
        }
    
        // count the user for each minute he was busy to
        // the answer array and count all users
        for (const [k, v] of D) {
            Ans[v.size - 1] += 1;
        }
        
        return Ans;
};
