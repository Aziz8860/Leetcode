def makeFancyString(s: str) -> str:
    if len(s) < 3:
        return s
    
    res = []
    res.append(s[0])
    res.append(s[1])
    
    for i in range(2, len(s)):
        if s[i] == res[-1] and s[i] == res[-2]:
            continue
        res.append(s[i])

    return ''.join(res)


        


