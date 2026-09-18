# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
            index = len(nums) - n
        nums.pop(index) # <--- ye wala pop

        # 3. Wapas linked list banao
        if not nums:
            return None

        new_head = ListNode(nums[0])
        curr = new_head
        for val in nums[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return new_head