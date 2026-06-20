from io import StringIO


class Solution:
    def encode(self, strs: list[str]) -> str:
        parts = [f"{len(strs)}\n"]
        for s in strs:
            parts.append(f"{len(s)}\n")
            parts.append(f"{s}\n")
        return "".join(parts)

    def decode(self, s: str) -> list[str]:
        dec_strs = []
        with StringIO(s) as f:
            num_strs = int(f.readline())
            for _ in range(num_strs):
                str_len = int(f.readline())
                dec_strs.append(f.read(str_len))
                f.seek(f.tell() + 1)
        return dec_strs
