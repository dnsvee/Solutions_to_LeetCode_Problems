/*
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/
*/
var levelOrderBottom = function(root) {
    var R = []; // array of lists for each depth
    
    // l is depth of search
    var dive = function(r, l) {
        R[l] = R[l] || [];
        R[l].push(r.val);
        
        if (r.left)  
            dive(r.left,  l + 1);
        
        if (r.right) 
            dive(r.right, l + 1)
    };
    
    if (root) 
        dive(root, 0)
    
    return R.reverse();
};
