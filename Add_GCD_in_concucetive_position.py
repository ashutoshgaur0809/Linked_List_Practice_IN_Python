# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Extract values from the linked list into a list
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        
        # Step 2: Calculate GCDs for consecutive pairs
        gcd_list = []
        for i in range(len(lst) - 1):
            gcd_value = math.gcd(lst[i], lst[i + 1])
            gcd_list.append(gcd_value)
        
        # Step 3: Interleave lst and gcd_list into a new list ans
        ans = []
        for i in range(len(lst)):
            ans.append(lst[i])  # Add original value
            if i < len(gcd_list):
                ans.append(gcd_list[i])  # Add corresponding GCD value
        
        # Step 4: Build the final linked list from the ans list
        dummy = ListNode(0)
        temp = dummy
        for value in ans:
            temp.next = ListNode(value)
            temp = temp.next
        
        return dummy.next



# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.
# Example 2:


# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
