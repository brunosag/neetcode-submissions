class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        return [x[0] for x in heapq.nlargest(k, freq.items(), lambda x: x[1])]
