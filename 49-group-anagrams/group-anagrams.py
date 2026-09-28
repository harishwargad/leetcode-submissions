class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}

        for i in strs:
            sortedS = ''.join(sorted(i))


            if sortedS not in res:
                res[sortedS] = []

            res[sortedS].append(i)
        return list(res.values())