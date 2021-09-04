/*
https://leetcode.com/problems/partition-labels/
*/
var partitionLabels = function(s) {
    let M = new Map();
    // make a map with key of single character and value is pair of numbers 
    // denoting range of first and last occurence of char in  s
    s.split('').forEach((c, i) => {
        let v = M.get(c) || [i, i];
        v[1] = (v) ? i : v[1];
        M.set(c, v);
    });

    // combine overlapping ranges 
    
    // m0 is current range
    m0 = M.get(s[0]) 
    
    let R = []       // result array
    
    for (const [k, v] of M) {
        // check if ranges overlap
        if (v[0] > m0[1]) {
            // if not push current range to result array
            R.push(m0);
            m0 = v; // next range becomes current range
        } else {
            // extend current range to include next range
            m0[1] = Math.max(m0[1], v[1])
        }
    }
    
    // calculate length of each range and return result
    return [...R, m0].map(([a,b]) => b - a + 1);
};
