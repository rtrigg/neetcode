"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.
"""


class Solution:
    """
    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    """

    @staticmethod
    def isValid(s: str) -> bool:
        """Fine valid parenthesis strings"""
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}
        for paren in s:
            if len(stack) == 0:
                if paren in pairs:
                    return False
                else:
                    stack.append(paren)
            elif paren in pairs and pairs[paren] == stack[-1]:
                stack.pop()
            else:
                stack.append(paren)
        return len(stack) == 0


if __name__ == "__main__":
    assert not Solution.isValid(")[]{}}")
    assert not Solution.isValid("(]{}}")
    assert not Solution.isValid("()[]{}}")
    assert not Solution.isValid("()[]{}}")
    assert Solution.isValid("()[]{}")
    assert Solution.isValid("()[]{}({[]})")
