class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack

    # def isValid(self, s: str) -> bool:
    #     if len(s) % 2 != 0:
    #         return False

    #     stack = []

    #     for c in s:
    #         if c == '(' or c == '{' or c == '[':
    #             stack.append(c)

    #         if c == ')' or c == '}' or c == ']':
    #             if not stack:
    #                 return False
                
    #             t = stack.pop() 
                
    #             if t == '(' and c != ')':
    #                 return False
    #             elif t == '{' and c != '}':
    #                 return False
    #             elif t == '[' and c != ']':
    #                 return False
            
    #     return len(stack) == 0
                
