# https://leetcode.com/problems/two-sum/description/
"""
1. Two Sum
Solved
Easy
Topics
Companies
Hint

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.hash(nums, target)

    # hash y = target - x
    def hash(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in seen:
                return [index, seen[diff]]
            else:
                seen[nums[index]] = index

    # O(n2)
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
