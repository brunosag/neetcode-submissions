class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i, s in enumerate(strs):
            d[''.join(sorted(s))].append(i)
        return [[strs[i] for i in gp] for gp in d.values()]
