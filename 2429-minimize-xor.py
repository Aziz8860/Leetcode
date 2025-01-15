def minimizeXor(num1: int, num2: int) -> int:
    def count_bits(n):
        res = 0
        while n > 0:
            # 0101
            # 0001 &

            res += 1 & n
            n = n >> 1
        return res
    
    cnt1, cnt2 = count_bits(num1), count_bits(num2)
    x = num1
    i = 0 # sebagai pointer

    # Remove least significant bit
    while cnt1 > cnt2:
        if x & (1 << i):
            cnt1 -= 1
            x = x ^ (1 << i) # flip with xor
        i += 1

    # Add least significant bit
    while cnt1 < cnt2:
        if x & (1 << i) == 0:
            cnt1 += 1
            x = x | (1 << i) # flip with or
        i += 1
    
    return x
    