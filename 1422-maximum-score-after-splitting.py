def maxScore(s: str) -> int:
    def count_0(s: str) -> int:
        return s.count('0')
    
    def count_1(s: str) -> int:
        return s.count('1')

    l, r = 0, len(s)-1
    res = 0

    for i in range(len(s)-1):
        left = count_0(s[0:(i+1)])
        right = count_1(s[-r:])
        
        res = max(res, left + right)

        l += 1
        r -= 1

    return res