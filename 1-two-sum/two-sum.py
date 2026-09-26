class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [i, indices[diff]]
            indices[n] = i
        return []