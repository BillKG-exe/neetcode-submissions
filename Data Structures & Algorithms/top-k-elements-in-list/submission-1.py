class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        results = []

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in dic.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)

                if len(results) == k:
                    return results
        