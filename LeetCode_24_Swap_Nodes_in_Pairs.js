// https://leetcode.com/problems/swap-nodes-in-pairs/
var swapPairs = function(head) {
    let last = null;
    
    let cur  = head;
    try {
        while (cur.next) {
            let n    = cur.next;
            cur.next = cur.next.next;
            n.next   = cur;
            if (last) {
                last.next = n;
                last = n;
            } else {
                head = n;
            }
            last = cur;
            cur  = cur.next;
        }
    } catch(err) {}
    
    return head;
};
