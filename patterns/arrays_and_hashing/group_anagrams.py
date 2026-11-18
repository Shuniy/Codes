# Anagrams are the words with same alphabets arranged differently

# n = length of word and w is number of words

# Time : O(w * nlogn + n * wlogw)
# Space : O(n * w)
def group_anagrams(words):
    if len(words) == 0:
        return []

    sorted_words = ["".join(sorted(word)) for word in words]
    indices = [i for i in range(len(words))]

    # Sorted indices according to sorted words
    indices.sort(key = lambda x : sorted_words[x])

    result = []
    current_anagram_group = []

    current_anagram = sorted_words[indices[0]]
    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if sorted == current_anagram:
            current_anagram_group.append(word)
            continue

        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word

    result.append(current_anagram_group)
    return result


# Time : O(w * nlogn)
# Space : O(w * n)
def group_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())