from collections import Counter, defaultdict


def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
    # Populate count_2 with maximum counts of characters in words2
    count_2 = defaultdict(int)
    for w in words2:
        count_w = Counter(w)
        for c, cnt in count_w.items():
            count_2[c] = max(count_2[c], cnt)

    res = []
    # Iterate through words1 and check the conditions
    for w in words1:
        count_w = Counter(w)
        for c, cnt in count_2.items():
            if count_w[c] < cnt:
                break  # Exit the loop if a condition is not met
        else: # This executes only if no break occurred. The else is tied to the for loop, not an if statement.
            res.append(w)  # Append to res only if no break occurred

    return res

    # Alternative
    # # STEP-1: Find freq of every word in words2
    # freq_words2 = [0] * 26
    # for word in words2:
    #     freq = [0] * 26
    #     for c in word:
    #         freq[ord(c) - ord('a')] += 1
    #     freq_words2 = [max(freq_words2[i], freq[i]) for i in range(26)]

    # # STEP-2: Find universal words in words1
    # universal_words = []
    # for word in words1:
    #     freq_word = [0] * 26
    #     for c in word:
    #         freq_word[ord(c) - ord('a')] += 1
    #     if all(freq_word[i] >= freq_words2[i] for i in range(26)):
    #         universal_words.append(word)
    # return universal_words