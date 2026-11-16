class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results, sol = [], []

        m = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(i=0):
            if len(sol) == len(digits):
                results.append("".join(sol[:]))
                return

            for l in m[digits[i]]:
                sol.append(l)
                backtrack(i+1)
                sol.pop()
        
        if digits:
            backtrack()
        
        return results
            