
/*
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
*/
var evaluate = function(s, knowledge) {
    let K = new Map();
    
    for (let [k, v] of knowledge) {
        K.set(k, v);
    }
    
    // replace a bracket pair if it's key is found
    // in the knowledge dict
    s = s.replace(/\((\w+)\)/g, (m, p1) => {
        return K.get(p1) || '?'
    });
    
    return s;
};
