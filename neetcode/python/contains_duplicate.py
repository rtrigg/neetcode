"""
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
"""


class Solution:
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    assert Solution.containsDuplicate([1, 1, 2, 3, 4])
    assert not Solution.containsDuplicate([1, 2, 3])
