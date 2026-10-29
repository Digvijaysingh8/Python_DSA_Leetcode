# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        temp=head
        c=0

        while c<k:
            if temp==None:
                return head
            temp=temp.next
            c+=1

        prev=self.reverseKGroup(temp,k)

        temp=head
        c=0

        while c<k:
            nxt_Node=temp.next
            temp.next=prev
            prev=temp
            temp=nxt_Node
            c+=1

        return prev             
        