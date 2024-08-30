# https://leetcode.com/problems/palindrome-linked-list/description/
"""
Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.



Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false



Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle_node = self.getMiddle(head)
        reverse_of_middle = self.reverseList(middle_node)

        current_rev = reverse_of_middle
        current = head
        while current_rev:
            if current_rev.val != current.val:
                return False

            current_rev = current_rev.next
            current = current.next
        return True

    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list
