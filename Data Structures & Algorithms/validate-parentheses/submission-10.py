class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif mapping[char] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0
