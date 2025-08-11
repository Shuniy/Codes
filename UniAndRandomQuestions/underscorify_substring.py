# Worst Case : string : tatatata..... and substring to repalce "t"
# We have to put "-" after every t
# Space : O(n) Worst Case : O(n ** l) l is the length of single location array roughly
# Time : Depends heavily on the string and replacing string but roughly
# O(n * (n + m))

def underscorify_substring(string, substring):
    locations = collapse(get_locations(string, substring))

    return underscorify(locations, string)

def underscorify(locations, string):
    locations_index = 0
    string_index = 0
    in_between_underscores = False

    final_characters = []
    i = 0

    while string_index < len(string) and locations_index < len(locations):
        if string_index == locations[locations_index][i]:
            final_characters.append("_")
            in_between_underscores = not in_between_underscores

            if not in_between_underscores:
                locations_index += 1
            i = 0 if i == 1 else 1
        
        final_characters.append(string[string_index])
        string += 1

    if locations_index < len(locations):
        final_characters.append("_")
    elif string_index < len(string):
        final_characters.append(string[string_index:])

    return "".join(final_characters)

def get_locations(string, substring):
    locations = []
    start_index = 0

    while start_index < len(string):
        next_index = string.find(substring, start_index)

        if next_index != -1:
            locations.append([next_index, next_index + len(substring)])
            start_index = next_index + 1

        else:
            break
    
    return locations

def collapse(locations):
    if not len(locations):
        return locations

    new_locations = [locations[0]]
    previous = new_locations[0]

    for i in range(1, len(locations)):
        current = locations[i]

        if current[0] <= previous[1]:
            previous[1] = current[1]

        else:
            new_locations.append(current)
            previous = current
    return new_locations
