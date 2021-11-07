'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
class Solution:
    def isValid(self, s: str):
        stack = []

        for item in s:
            print(item)
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if top == '[' and item == ']' or top == '{' and item == '}' or top == '(' and item ==')':
                    stack.pop()
                else:
                    return False
                
        if not stack:
            return True
        return False

test = Solution()
print(test.isValid('(])'))