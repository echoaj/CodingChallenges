"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""


def isValid(s: str) -> bool:
    pairs = {'(':')',
             '[':']',
             '{':'}'}

    stack = []

    for cur in s:
        empty = not stack
        if empty and cur not in pairs:  # Rule 1: when stack is empty and cur is closing paranthese
            return False
        elif cur not in pairs:          # Rule 2: A miss match
            top = stack[-1]
            if pairs[top] == cur:
                stack.pop()
            else:
                return False

        elif cur in pairs:
            stack.append(cur)

    if stack:                           # Rule 3: stack not empty
        return False
    return True




print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("()[]{}"))