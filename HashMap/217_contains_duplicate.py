"""
LeetCode Problem: 217. Contains Duplicate

💡 Problem:
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element is distinct.

Example:
nums = [1,2,3,1] → True
nums = [1,2,3,4] → False

🕒 Time Complexity: O(n)
📦 Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums):
        seen = set()   # store values we already visited

        for num in nums:
            if num in seen:
                return True   # duplicate found
            seen.add(num)

        return False   # no duplicates
🧪 Example Test:
print(Solution().containsDuplicate([1,2,3,1]))  # True
print(Solution().containsDuplicate([1,2,3,4]))  # False

