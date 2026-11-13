class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        results, sol = [], []

        def b(it):
            if it == size:
                results.append(sol[:])
                return
            
            for i in range(size):
                if nums[i] in sol:
                    continue
                
                sol.append(nums[i])
                b(it+1)
                sol.pop()
        
        b(0)
        return results