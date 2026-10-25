class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area



# Brute force solution
    # def maxArea(self, heights: List[int]) -> int:
    #     max_h = 0

    #     for i in range(len(heights)):
    #         for j in range(len(heights)):
    #             if i == j:
    #                 continue
                
    #             h = abs(i - j) * min(heights[i], heights[j])

    #             if h > max_h:
    #                 max_h = h

    #     return max_h