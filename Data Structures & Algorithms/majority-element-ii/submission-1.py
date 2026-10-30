class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        top = len(nums) // 3
        count = 1
        results = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                if count > top:
                    results.append(nums[i-1])
                count = 1
                pass

        if count > top:
            results.append(nums[-1])

        return results