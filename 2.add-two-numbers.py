#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val
    

def getnumber(link: ListNode, index, cur) -> int:
    if(link.next == NULL):
        return 0
    return getnumber(link.next, index+1, cur+((link.val)*(10**index)))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return getnumber(l1, 0, 0 ) + getnumber(l2, 0, 0 )
# @lc code=end

