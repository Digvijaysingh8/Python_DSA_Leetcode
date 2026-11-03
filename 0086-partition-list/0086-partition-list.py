# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        sm=ListNode(0)
        lg=ListNode(0)

        sm_t=sm
        lg_t=lg

        cur=head


        while cur:
            next_node=cur.next
            cur.next=None
            if cur.val<x:
                sm_t.next=cur
                sm_t=sm_t.next
            else:
                lg_t.next=cur
                lg_t=lg_t.next

            cur=next_node

        sm_t.next=lg.next
      

        return sm.next            


        