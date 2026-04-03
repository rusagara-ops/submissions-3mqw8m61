# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head

        # finding the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # then slicing the list into two
        prev = None
        curr = slow.next
        slow.next = None

        # reversing l2 after slicing
        
        while curr:
            nextt_f = curr.next
            curr.next = prev
            prev = curr
            curr = nextt_f

        # now we have l2 and l1
        l2 = prev
        l1 = head
        # now we are going to merge the two lists in place without creating a new node

        while l1 and l2:
            l1_n = l1.next
            l2_n = l2.next

            l1.next = l2
            if l1_n:
                l2.next = l1_n
            l2 = l2_n
            l1 = l1_n
        
            

        



        