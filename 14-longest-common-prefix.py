def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    # print(strs)
    ans = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            # print("step ke ", i)
            # print("strs[0][i]", strs[0][i], "dari", strs[0])
            # print("strs[-1][i]", strs[-1][i], "dari", strs[-1])
            ans += strs[0][i]
        else:
            break
    return ans


    # Leetcode
    # res = ""
    # for i in range(len(strs[0])):
    #     for s in strs:
    #         if i == len(s) or s[i] != strs[0][i]:
    #             return res
    #     res += strs[0][i]
    # return res

longestCommonPrefix(["flight", "freal", "flow","flight"]) # "fl"