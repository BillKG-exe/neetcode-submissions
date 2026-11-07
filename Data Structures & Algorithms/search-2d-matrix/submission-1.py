class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            mid = t + (b - t) // 2

            if target < matrix[mid][0]:
                # What should happen to b?
                b = mid - 1

            elif target > matrix[mid][-1]:
                t = mid + 1

            else:
                l, r  = 0, len(matrix[mid]) - 1

                while l <= r:
                    m = l + (r - l) // 2

                    if matrix[mid][m] == target:
                        return True

                    if target > matrix[mid][m]:
                        l = m + 1
                    else:
                        r = m - 1
                return False
        return False