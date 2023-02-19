
def CountOccurencesAnagrams(text: str, word: str):
    i = 0
    result = 0
    k = len(word)
    hashmap = {}
    for item in word:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

    # So, we dont have to traverse all the hashmap to check for zero
    hashmapCount = len(hashmap)
    for j in range(len(text)):
        if text[j] in hashmap:
            hashmap[text[j]] -= 1
            if hashmap[text[j]] == 0:
                hashmapCount -= 1

        if j - i + 1 < k:
            continue
        else:
            if hashmapCount == 0:
                result += 1
            if text[i] in hashmap:
                hashmap[text[i]] += 1
                if hashmap[text[i]] == 1:
                    hashmapCount += 1
            i += 1

    return result

text: str = "forxxorfxdofr"
word: str = "for"

print(CountOccurencesAnagrams(text, word))