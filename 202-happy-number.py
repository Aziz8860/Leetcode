class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(n):
            res = 0
            while n > 0:
                digit_akhir = n % 10
                res += (digit_akhir)**2
                n //= 10
            return res

        seen = set()
    
        while n != 1 and n not in seen:
            seen.add(n)
            n = squares(n)

        return n == 1