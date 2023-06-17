"""
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    """Solve binary search problem"""

    @staticmethod
    def search(nums: list[int], target: int) -> int:
        """Return index of target"""
        low = 0
        high = len(nums) - 1
        mid = (len(nums) - 1) // 2
        while high >= low:
            if __debug__:
                print(f"{low=}, {mid=}, {high=}")
            if target > nums[mid]:
                low = mid + 1
                mid = (low + high) // 2
            elif target < nums[mid]:
                high = mid - 1
                mid = (low + high) // 2
            elif target == nums[mid]:
                return mid
        return -1


if __name__ == "__main__":
    assert Solution.search(nums=[5], target=5) == 0
    assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert Solution.search(nums=[0, 3, 5, 9, 12], target=9) == 3
    assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
