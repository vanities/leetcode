# https://leetcode.com/problems/majority-element/description/
"""
169. Majority Element
Solved
Easy
Topics
Companies

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# this one is interesting because you could just do...


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


# but this was my initial thought
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        max_value = 0
        max_index = 0
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
            if h[num] > max_value:
                max_value = h[num]
                max_index = num

        return max_index
