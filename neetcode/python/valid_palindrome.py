"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        for i, v in enumerate(s):
            if v != s[-i - 1]:
                return False
        return True


if __name__ == "__main__":
    assert Solution.isPalindrome("A man, a plan, a canal: Panama")
    assert Solution.isPalindrome("racecar")
    assert not Solution.isPalindrome("holy smokes")
    assert Solution.isPalindrome("c#dc")
