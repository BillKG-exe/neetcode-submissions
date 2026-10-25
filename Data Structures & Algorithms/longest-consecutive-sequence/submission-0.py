class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_seq = 0
        
        seq = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] - nums[i-1] == 1:
                seq += 1
            elif nums[i] - nums[i-1] != 1:
                max_seq = max(max_seq, seq)
                seq = 0

        return max(max_seq, seq) + 1