class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                right = result.pop()
                left = result.pop()

                if tokens[i] == '+':
                    result.append(left + right)
                elif tokens[i] == '-':
                    result.append(left - right)
                elif tokens[i] == '*':
                    result.append(left * right)
                elif tokens[i] == '/':
                    result.append(int(left / right))
            else:
                result.append(int(tokens[i]))

        return result.pop()

        