class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            str_len = int(s[i:j])

            start = j + 1
            end = start + str_len
            result.append(s[start:end])

            i = end

        return result
