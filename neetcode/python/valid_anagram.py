"""
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.
"""

from collections import Counter


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert Solution.isAnagram("elbow", "below")
    assert not Solution.isAnagram("cat", "mat")
    assert not Solution.isAnagram("bbbb", "bb")
    assert not Solution.isAnagram("bbba", "bbaa")
