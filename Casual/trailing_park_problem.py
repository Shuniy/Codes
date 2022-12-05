"""
'.' = -2
'#' = block
'*' = 5
reach to end with minimum energy of 5
if block can change row without energy loss
"""
def magical_park(park, m, n, k, s):
    success = True
    for i in range(m):
        for j in range(n):
            c = park[i][j]

            if (s < k):
                success = False
                break
            if c == '*':
                s += 5
            elif c == ".":
                s -= 2
            else:
                break
            if j != n - 1:
                s -= 1
    if success:
        print('yes')
        print(s)
    else:
        print('No')
        return None

m = n = k = s = 0

m, n, k, s = int(input("Enter the values").split())

park = []

for i in range(m):
    ted = []
    for j in range(n):
        ted.append(j)
    park.append(ted)

magical_park(park, m, n, k, s)
