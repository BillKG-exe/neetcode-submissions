class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # Check whether the window is valid
            max_freq = max(count.values())
            replace_count = (right - left + 1) - max_freq
            
            # Shrink the window if necessary
            if replace_count > k:
                count[s[left]] -= 1
                left += 1

            # Update max_len
            max_len = max(max_len, right - left + 1)
        
        return max_len