class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        seen = set()
        max_count, count = 0, 0

        for unique_num in unique_nums:
            count = 0

            num = unique_num
            while num in unique_nums and num not in seen:
                count += 1
                seen.add(num)
                num += 1

            num = unique_num - 1
            while num in unique_nums and num not in seen:
                count += 1
                seen.add(num)
                num -= 1

            if count > max_count:
                max_count = count

        return max_count
