class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        requested = defaultdict(lambda: None)
        for i, num in enumerate(nums):
            if requested[num] is not None:
                return [requested[num], i]
            else:
                requested[target - num] = i
