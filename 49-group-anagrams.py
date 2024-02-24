def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dict = {}

    for s in strs:
        # Sort the string and convert it to a tuple to use as a dictionary key
        key = tuple(sorted(s))
        
        if key not in dict:
            dict[key] = [s]
        else:
            dict[key].append(s)

    # The values of the dictionary are the grouped anagrams
    res = list(dict.values())
    return res

groupAnagrams(["eat","tea","tan","ate","nat","bat"])