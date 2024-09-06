class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        ans = []
        for i in lst:
            if i not in nums:
                ans.append(i)
        d = ListNode(0)
        temp = d
        while ans:
            temp.next = ListNode(ans.pop(0))
            temp = temp.next
        return d.next  

# Example 1:

# Input: nums = [1,2,3], head = [1,2,3,4,5]

# Output: [4,5]

# Explanation:



# Remove the nodes with values 1, 2, and 3.

# Example 2:

# Input: nums = [1], head = [1,2,1,2,1,2]

# Output: [2,2,2]

# Explanation:



# Remove the nodes with value 1.

# Example 3:

# Input: nums = [5], head = [1,2,3,4]

# Output: [1,2,3,4]

# Explanation:



# No node has value 5.
