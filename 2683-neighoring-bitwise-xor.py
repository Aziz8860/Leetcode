def doesValidArrayExist(derived: list[int]) -> bool:
    xor_sum = 0
    for n in derived:
        xor_sum ^= n # Accumulate XOR of each element

    # If the XOR sum is 0, a valid original array exists
    return xor_sum == 0
    
    # Effective solution
    # first = 0
    # last = 0

    # for n in derived:
    #     if n:
    #         last = ~last

    # return first == last