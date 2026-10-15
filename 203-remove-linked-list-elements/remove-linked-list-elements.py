# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        node=ListNode(0)
        node.next=head
        current=node
        while current.next:
            
            if val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return node.next
            