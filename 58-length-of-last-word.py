def lengthOfLastWord(s: str) -> int:
    t = s.split()
    ans = len(t[-1])
    return ans


lengthOfLastWord("Hello    World     ") # 5
# lengthOfLastWord(" ") # 0
# lengthOfLastWord("a ") # 1
# lengthOfLastWord("luffy is still joyboy") # 6