class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for i in strs:
            sortedS = "".join(sorted(i))
            res[sortedS].append(i)
        return list(res.values())
