class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        results, sol = [], []

        def b(i):
            if i == size:
                results.append(sol[:])
                return

            b(i+1)
            sol.append(nums[i])
            b(i+1)
            sol.pop()
        b(0)
        return results