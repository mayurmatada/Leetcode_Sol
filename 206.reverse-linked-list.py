# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        cur = ListNode(5001, head)
        while (cur.next != None):
            vals.append(cur.next.val)
            cur.next = cur.next.next
        cur.next = head
        while (cur.next != None):
            cur.next.val = vals.pop()
            cur.next = cur.next.next
        return head
