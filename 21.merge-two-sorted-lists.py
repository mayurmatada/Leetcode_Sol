#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addtolast(self, val) -> Optional[ListNode]:
        cur = ListNode(val = val, next= None)
        self.next = cur
        return cur


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = []
        
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1

        while(list1 != None and list2 != None):
            if(list1.val < list2.val):
                l3.append(list1.val)
                list1 = list1.next

            elif(list2.val < list1.val):
                l3.append(list2.val)
                list2 = list2.next
            
            else:
                l3.append(list1.val)
                l3.append(list2.val)
                list1 = list1.next
                list2 = list2.next

        if(list1 == None):
            while(list2 != None):
                l3.append(list2.val)
                list2 = list2.next
        elif(list2 ==  None):
            while(list1 != None):
                l3.append(list1.val)
                list1 = list1.next
                
        head = cur = ListNode(l3[0])
        
        for i in l3[1:]:
            cur = cur.addtolast(i)
            
        return head
# @lc code=end

