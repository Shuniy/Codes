def CountOccurencesAnagrams(text: str, word: str):
    """
    Count the number of occurrences of anagrams of a word within a text string.

    Parameters:
    - text: a string representing the text in which to search for anagrams
    - word: a string representing the word to find anagrams of within the text

    Returns:
    - An integer representing the count of occurrences of anagrams of the word within the text
    """
    i = 0
    result = 0
    k = len(word)
    hashmap = {}
    for item in word:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

    hashmap_count = len(hashmap)
    for j, item in enumerate(text):
        if item in hashmap:
            hashmap[item] -= 1
            if hashmap[item] == 0:
                hashmap_count -= 1
        if j - i + 1 < k:
            continue
        if hashmap_count == 0:
            result += 1
        if text[i] in hashmap:
            hashmap[text[i]] += 1
            if hashmap[text[i]] == 1:
                hashmap_count += 1
        i += 1

    return result


TEXT: str = "forxxorfxdofr"
WORD: str = "for"

print(CountOccurencesAnagrams(TEXT, WORD))
