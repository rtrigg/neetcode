"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""


class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            if target - v in hash_map:
                return i, hash_map[target - v]
            else:
                hash_map[v] = i


if __name__ == "__main__":
    assert sorted(Solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(Solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(Solution.twoSum([3, 3], 6)) == [0, 1]
