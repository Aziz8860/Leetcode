def findThePrefixCommonArray(A:list[int], B: list[int]) -> list[int]:
    res = []
    set_a, set_b = set(), set()
    common_count = 0

    for i in range(len(A)):
        if A[i] == B[i]:
            common_count += 1
        else:
            if A[i] in set_b:
                common_count += 1
            if B[i] in set_a:
                common_count += 1

        set_a.add(A[i])
        set_b.add(B[i])
        res.append(common_count)

    return res