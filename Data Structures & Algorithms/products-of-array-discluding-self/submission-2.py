class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prefix[0] = nums[0] or 1
        suffix[-1] = nums[-1] or 1
        zero_idx = None

        for i in range(1, len(nums)):
            if nums[i] == 0:
                if zero_idx is None:
                    zero_idx = i
                    prefix[i] = prefix[i - 1]
                else:
                    return [0] * len(nums)
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            if i == zero_idx:
                suffix[i] = suffix[i + 1]
            else:
                suffix[i] = suffix[i + 1] * nums[i]

        result = [0] * len(nums)
        if zero_idx is None:
            result[0] = suffix[1]
            result[-1] = prefix[-2]
            for i in range(1, len(nums) - 1):
                result[i] = prefix[i - 1] * suffix[i + 1]
        else:
            result[zero_idx] = suffix[0]
        return result
