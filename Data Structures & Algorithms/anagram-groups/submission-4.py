class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gp = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for char in s:
                letters[ord(char) - ord('a')] += 1
            gp[tuple(letters)].append(s)
        return list(gp.values())
