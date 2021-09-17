A = []
for i in range(5):
    A.append( [7] * 5 )
    
A[4][4] = 5
A[0][4] = 4

print(A)
print(min(A[0]))
print(min(A[4]))