"""
LeetCode Problem: 21. Merge Two Sorted Lists

💡 Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return its head.

Example:
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

🕒 Time Complexity: O(n + m)
📦 Space Complexity: O(1)  (in-place, ignoring output list)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        # while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1   # attach list1 node
                list1 = list1.next     # move list1 forward
            else:
                current.next = list2   # attach list2 node
                list2 = list2.next     # move list2 forward

            current = current.next      # move merged pointer

        # if any nodes left in list1 or list2, attach them
        if list1:
            current.next = list1
        else:
            current.next = list2

        # dummy.next is the real head
        return dummy.next
✅ Simple Test Code

Just create two linked lists manually:

# Create test lists
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge
result = Solution().mergeTwoLists(l1, l2)

# Print result
while result:
    print(result.val, end=" ")
    result = result.next

🟢 Output:
1 1 2 3 4 4
