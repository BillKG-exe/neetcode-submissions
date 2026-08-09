class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in seen:
                seen[num] = [i]
            else:
                seen[num].append(i)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen and (i not in seen[diff] or len(seen[diff]) > 1):
                if i not in seen[diff]:
                    return [i, seen[diff][0]]
                else: 
                    return [i, seen[diff][1]]

        return []
