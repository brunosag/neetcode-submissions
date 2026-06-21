class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_idx = None

        for i, num in enumerate(nums):
            if num == 0:
                if zero_idx is None:
                    zero_idx = i
                else:
                    return [0] * len(nums)
            else:
                product *= num

        if zero_idx is None:
            return [(product // num) for num in nums]
        else:
            result = [0] * len(nums)
            result[zero_idx] = product
            return result
