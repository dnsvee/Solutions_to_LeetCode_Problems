# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head, n):
        def visit(prev, node):
            # visit until the end and backtracking while counting nodes
            # remove the requested node
            if not node:
                  return 1
                
            count = visit(node, node.next)
            
            if count == n:
                prev.next = node.next
                
            return count + 1    
            
                
        try:
            visit(None, head)
            
        except:
            return head.next
        
        else:
            return head
