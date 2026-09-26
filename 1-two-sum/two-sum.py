class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numberSet = {}

        for i in range(len(nums)):
            numberSet[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numberSet and numberSet[complement] != i:
                return [i, numberSet[complement]]

        return []