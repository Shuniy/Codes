def string_reverser(our_string):
    string_position = len(our_string) - 1
    reversed_string = ''

    while string_position >= 0:
        reversed_string += our_string[string_position]
        string_position -= 1

    return reversed_string

def word_flipper(our_string):
    our_string_split = our_string.split(sep=' ')
    words_reversed = []

    for word in our_string_split:
        words_reversed.append(string_reverser(word))

    return " ".join(words_reversed)

print(word_flipper("i dont care"))
