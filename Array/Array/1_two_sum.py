Array/1_two_sum.py
"""
LeetCode Problem: 1. Two Sum

💡 Problem:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Example:
nums = [3, 2, 4], target = 6 → Output: [1, 2]

🕒 Time Complexity: O(n)
📦 Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}  # store number:index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []  # no solution found
