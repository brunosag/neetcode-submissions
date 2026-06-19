class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gp = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            gp[sorted_s].append(s)
        return list(gp.values())
