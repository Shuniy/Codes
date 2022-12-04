# -*- coding: utf-8 -*-
"""
Strassen
"""

def Strassen(mx1, mx2, n):
    a = b = c = d = e = f = g = h = P1 = P2 = P3 = P4 = P5 = P6 = P7 = 0 
    Q1 = Q2  = Q3 = Q4 = i = j = 0
    R = []

    a = mx1[0][0] 
    b = mx1[0][1] 
    c = mx1[1][0] 
    d = mx1[1][1] 
    e = mx2[0][0] 
    f = mx2[0][1] 
    g = mx2[1][0] 
    h = mx2[1][1] 

    P1 = a *( f - h ) 
    P2 = ( a + b ) * h 
    P3 = ( c + d ) * e 
    P4 = d * ( g - e ) 
    P5 = ( a + d ) * ( e + h ) 
    P6 = ( b - d ) * ( g + h ) 
    P7 = ( a - c ) * ( e + f ) 

    Q1 = P5 + P4 + P6 - P2 
    Q2 = P1 + P2 
    Q3 = P3 + P4 
    Q4 = P1 + P5 - P3 - P7 
    
    for i in range(2):
        MX = []
        for j in range(2):
            MX.append(0)
        R.append(MX)

    R[0][0] = Q1   
    R[0][1] = Q2   
    R[1][0] = Q3   
    R[1][1] = Q4;

    for i in range(n):
        for j in range(n):
            print(R[i][j], end = " ")
        print(" ")    


MX1 = []
MX2 = []
i = j = 0
  
print("Enter the elements of the first matrix: ")
for i in range(2):
    MX = []
    for j in range(2):
        c1 = input()
        MX.append(int(c1))
    MX1.append(MX)    
        
print("Enter the elements of the second matrix: ")
for i in range(2):
    MX = []
    for j in range(2):
        c2 = input()
        MX.append(int(c2))
    MX2.append(MX)    
   
print("Entered First Matrix is : ")
for i in range(2): 
    for j in range(2): 
        print(MX1[i][j], end = " ") 
    print(" ")

print("Entered Second Matrix is : ")
for i in range(2): 
    for j in range(2): 
        print(MX2[i][j], end = " ") 
    print(" ")    

print("The resultant matrix is :")
Strassen(MX1,MX2,2);
