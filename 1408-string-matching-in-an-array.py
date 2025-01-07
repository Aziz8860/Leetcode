def stringMatching(words: list[str]) -> list[str]:
    res = []

    # O(n^2) solution
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            if words[i] in words[j]:
                res.append(words[i])
                break
    return res

    # Best practice: 
    # 1. KMP, atau
    # 2. Rabin Karp

