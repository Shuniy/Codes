# Time : O(n * M^2 + nlogn) // m is the length of longest string and n is the number of strings
# Space : O(n * m)

def longest_string_chain(strings):
    string_chains = {}

    for string in strings:
        string_chains[string] = {'next_string' : "", 'max_chain_length' : 1}

    sorted_strings = sorted(strings, key = len)

    for string in sorted_strings:
        find_longest_string_chain(string, string_chains)

    return build_longest_string_chain(strings, string_chains)

def build_longest_string_chain(strings, string_chains):
    max_chain_length = 0
    chain_starting_string = ""

    for string in strings:
        if string_chains[string]['max_chain_length'] > max_chain_length:
            max_chain_length = string_chains[string]['max_chain_length']
            chain_starting_string = string

        our_longest_string = []
        current_string = chain_starting_string
        while current_string != "":
            our_longest_string.append(current_string)
            current_string = string_chains[current_string]['next_string']

        return [] if len(our_longest_string) == 1 else our_longest_string


def find_longest_string_chain(string, string_chains):
    for i in range(len(string)):
        smaller_string = get_smaller_string(string, i)

        if smaller_string not in string_chains:
            continue
        update_longest_string_chain(string, smaller_string, string_chains)


def update_longest_string_chain(current_string, smaller_string, string_chain):
    smaller_string_chain_length = string_chain[smaller_string]['max_chain_length']
    current_string_chain_length = string_chain[current_string]['max_chain_length']

    if smaller_string_chain_length + 1 > current_string_chain_length:
        string_chain[current_string]['max_chain_length'] = smaller_string_chain_length + 1
        string_chain[current_string]['next_string'] = smaller_string

def get_smaller_string(string, index):
    return string[0: index] + string[index + 1:]