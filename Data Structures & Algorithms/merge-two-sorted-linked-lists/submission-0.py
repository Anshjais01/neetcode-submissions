# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify edge cases (like empty lists)
        dummy = ListNode()
        # 'tail' will point to the last node in our new merged list
        tail = dummy
        
        # Traverse both lists as long as neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move the tail pointer forward
            tail = tail.next
            
        # If one list is exhausted before the other, attach the remainder of the non-empty list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # The merged list starts at dummy.next
        return dummy.next