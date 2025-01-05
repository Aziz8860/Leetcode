# strings are evil
# jadi lebih baik pake integer aja
# + 26 biar selalu positif
# mod 26 biar selalu dalam range 0-25
def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
        # pelajarin lagi
        # asli ga paham yg prefix array
        # pelajarin lagi plis (06/01/2025)
        prefix_diff = [0] * (len(s) + 1)

        for left, right, d in shifts:
            prefix_diff[right + 1] += 1 if d else -1
            prefix_diff[left] += -1 if d else 1

        diff = 0
        res = [ord(c) - ord("a") for c in s] # 0-25

        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]

            res[i - 1] = (diff + res[i - 1] + 26) % 26

        s = [chr(ord("a") + n) for n in res]
        return "".join(s)

