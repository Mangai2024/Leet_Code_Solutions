"""
LeetCode Problem: 349. Intersection of Two Arrays

💡 Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be UNIQUE.

Example:
nums1 = [1,2,2,1]
nums2 = [2,2]
Output: [2]

🕒 Time Complexity: O(n + m)
📦 Space Complexity: O(n)
"""

class Solution:
    def intersection(self, nums1, nums2):
        # convert both arrays to sets (unique values only)
        set1 = set(nums1)
        set2 = set(nums2)

        # intersection of sets
        return list(set1 & set2)
Test 
print(Solution().intersection([1,2,2,1], [2,2]))  # [2]
print(Solution().intersection([4,9,5], [9,4,9,8,4]))  # [9,4] or [4,9]
