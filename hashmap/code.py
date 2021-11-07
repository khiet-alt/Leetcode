'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for index, item in enumerate(nums):
            remain = target - item
            if dict.get(remain) is not None:
                return [index, dict.get(remain)]
            
            dict[item] = index