class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        track = set()

        left, right = 0, 0

        while right < len(s):
            while s[right] in track:
                track.remove(s[left])
                left += 1

            track.add(s[right])
            max_len = max(max_len, len(track))

            right += 1

        return max_len