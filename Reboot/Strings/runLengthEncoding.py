def stringEncoding(string):
    encoded = ""
    i = 0
    n = len(string)
    while i < n:
        count = 1
        while i < n - 1 and string[i] == string[i + 1]:
            count += 1
            i += 1
        
        encoded  += string[i] + str(count) if count > 1 else string[i]
        i += 1
            
    if n <= len(encoded):
        return string
    
    return encoded
    

string = "aaaaabbbcccdddddaaabbcd"
print(stringEncoding(string))