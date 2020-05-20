import numpy as np

A = np.matrix([(0,1,0,0),(0.5,0,0,0),(0.5,0,0,1),(0,0,1,0)])
r = np.matrix([(0.25,0.25,0.25,0.25)]).T
#input your support
S = [1]
c = []
i = 1
#input your beta
beta =0.7

#Transform A, only teleport to S
for n in range(1,len(A)+1):
    if n in S:
        A[n-1] = A[n-1]*beta + (1-beta)/len(S)
    else:
        A[n-1] = A[n-1]*beta + 0

#Iteration
while True:
    c.append(r)
    r = np.around(np.dot(A,r),4)
    if i > 30:
        break
    print(f"This iteration{i},new Page Rank is :\n{r}")
    i += 1
