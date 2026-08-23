class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted in hash_table:
                hash_table[s_sorted].append(s)
            else:
                hash_table[s_sorted] = [s]

        return list(hash_table.values())


        