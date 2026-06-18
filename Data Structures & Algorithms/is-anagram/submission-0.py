class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)

        for char in s:
            letters[char] += 1
        for char in t:
            if letters[char] == 0:
                return False
            letters[char] -= 1

        if sum(letters.values()) == 0:
            return True
        else:
            return False
