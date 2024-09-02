# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]



Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n



Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""


# this is a set theory one with negating number
"""
Solution using Set Difference:
The set difference operation, denoted by A - B, returns a new set containing elements that are in set A but not in set B. In other words, it finds the elements that are present in A but missing in B.

To solve this problem using set difference, you can follow these steps:

    Create a set called allNumbers that contains all the integers from 1 to n (inclusive). This represents the complete set of numbers in the given range.

    Convert the input array nums into a set called numSet. This eliminates any duplicate elements and allows for efficient set operations.

    Perform the set difference operation allNumbers - numSet. This will give you a new set containing the integers that are present in allNumbers but missing in numSet, which represents the numbers that do not appear in nums.

    Convert the resulting set back to an array and return it as the output.

"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        position = 0
        for index in range(len(nums)):
            if nums[index] < 0:
                position = (-1 * nums[index]) - 1
            else:
                position = nums[index] - 1

            if nums[position] > 0:
                nums[position] = -1 * nums[position]

        for index in range(len(nums)):
            print(index, nums[index])
            if nums[index] > 0:
                answer.append(index+1)
        return answer
