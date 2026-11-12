class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results, sol = [], []
        size = len(nums)

        def backtrack(i, total):
            if total == target:
                results.append(sol[:])
                return
            
            if total > target or  i >= size:
                return

            sol.append(nums[i])
            backtrack(i, total + nums[i])
            
            sol.pop()

            backtrack(i+1, total)

        backtrack(0, 0)
        return results