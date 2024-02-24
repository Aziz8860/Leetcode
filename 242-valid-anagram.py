def isAnagram(s: str, t: str) -> bool:
    sDict = {}

    for i in s:
        sDict[i] = sDict.get(i, 0) + 1
    
    for j in t:
        sDict[j] = sDict.get(j, 0) - 1

    if all(value == 0 for value in sDict.values()):
        return True
    else:
        return False
    
    # neetcode's solution 1
    # if len(s) != len(t):
    #     return False
    
    # countS, countT = {}, {}

    # for i in range(len(s)):
    #     countS[s[i]] = countS.get(s[i], 0) + 1
    #     countT[s[i]] = countT.get(s[i], 0) + 1
    
    # for c in countS:
    #     if countS[c] != countT.get(c, 0):
    #         return False
    
    # return True
    # atau bisa juga pake library Counter
    # jadi cukup 1 line -> return Counter(s) == Counter(t)
    # penjelasan: Counter membuat hashmap juga


    # neetcode's solution 2
    # return sorted(s) == sorted(t)
    # penjelasan: jadi diurut dulu baru dibandingin
