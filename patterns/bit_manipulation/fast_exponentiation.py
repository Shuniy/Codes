# time : O(log(power)) + 1
def fastexponentitation(n, power):
    answer = 1
    
    while power:
        lastbit = power & 1
        if lastbit:
            answer *= n
        
        n = n * n
        power = power >> 1
    
    return answer
    
n = 2
power = 4
print(fastexponentitation(n, power))