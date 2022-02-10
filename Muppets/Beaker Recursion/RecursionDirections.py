# Print all the numbers from 0 to n and n to 0

# Method 1
# Top Bottom -> Execute first and then perform recursion
def recursionTopBottom(n):
    if n < 0:
        return 
    
    print(n)
    recursionTopBottom(n - 1)    
    
# Method 2
# Bottom Up -> Create all the recursion stacks and then execute
def recursionBottomUp(n):
    if n < 0:
        return 
    
    recursionBottomUp(n - 1)
    print(n)

n = 10
recursionTopBottom(n)
recursionBottomUp(n)