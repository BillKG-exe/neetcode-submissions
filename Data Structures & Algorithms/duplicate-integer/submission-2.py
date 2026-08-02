class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums)):
            if (i - 1 >= 0) and (sorted_nums[i - 1] == sorted_nums[i]):
                return True
        
        return False
