/*
https://leetcode.com/problems/merge-k-sorted-lists/
*/

// merge two lists at each time
var mergeKLists = function(lists) {
    if (!lists.length) return null;
    
    // dummy value for simplified algo
    if (lists.length == 1) lists.push(null);
    
    var merge = function(l1, l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        
        // h is dummy listnode to use as head of list
        let h = new ListNode(), c = h, n = null;

        while (l1 && l2) {
            // l1 must point to list with smallest val
            if (l1.val > l2.val) {
                [l1, l2] = [l2, l1];
            }

            // n == smallest val
            n  = l1;
            l1 = l1.next;
            
            c.next = n;
            c      = n;
        }

        // if one list is empty add remaining nodes from other list
        if (l2) c.next = l2;
        
        // strip dummy head
        return h.next;
    }

    // merge the two list into one list
    let r = lists.pop();
    
    while (lists.length) 
        r = merge(r, lists.pop());
    
    return r;
};