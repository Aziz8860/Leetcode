class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a_index = len(a) - 1
        b_index = len(b) - 1

        sisa = 0
        res = []

        while a_index >= 0 or b_index >= 0 or sisa:
            digit_a = int(a[a_index]) if a_index >= 0 else 0
            digit_b = int(b[b_index]) if b_index >= 0 else 0

            total = digit_a + digit_b + sisa
            hasil = total % 2
            sisa = total // 2

            res.insert(0, str(hasil))

            a_index -= 1
            b_index -= 1
        
        return "".join(res)