class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in freq_map.items():
            freq[count].append(num)
        
        top_k = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
