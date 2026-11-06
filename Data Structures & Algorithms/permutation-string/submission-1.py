class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)

        if k > n:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Initialize frequency arrays
        for i in range(k):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        # Slide the window
        for right in range(k, n):
            left = right - k

            # Remove character leaving the window
            count2[ord(s2[left]) - ord('a')] -= 1

            # Add character entering the window
            count2[ord(s2[right]) - ord('a')] += 1

            if count1 == count2:
                return True

        return False

    # Brute Force 
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     left, right = 0, len(s1) - 1

    #     sorted_s1 = sorted(s1)

    #     while right < len(s2):
    #         if sorted(s2[left:right+1]) == sorted_s1:
    #             return True

    #         left += 1
    #         right += 1

    #     return False 