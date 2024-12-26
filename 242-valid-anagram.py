def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
            return False
        
    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    return count_s == count_t
    
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
