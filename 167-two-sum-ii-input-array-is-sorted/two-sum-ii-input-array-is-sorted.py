class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        mp = defaultdict(list)

        for i in range(len(numbers)):
            temp = target - numbers[i]
            if mp[temp]:
                return [mp[temp], i+1]
            mp[numbers[i]] = i+1

        return []
