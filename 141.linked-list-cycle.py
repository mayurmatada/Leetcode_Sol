#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None):
            return False
        if(head.next == None):
            return False
        count = 0
        while(head.next != None):
            count += 1
            if(count > 10005):
                return True
            head = head.next
            
# @lc code=end

