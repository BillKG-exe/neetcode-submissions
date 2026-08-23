class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key in hash_table:
                hash_table[key].append(s)
            else:
                hash_table[key] = [s]

        return list(hash_table.values())