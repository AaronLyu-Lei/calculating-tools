import numpy as np

A = np.matrix([(0,1,0,0),(0.5,0,0,0),(0.5,0,0,1),(0,0,1,0)])
r = np.matrix([(0.25,0.25,0.25,0.25)]).T
v = np.matrix([(0.25,0.25,0.25,0.25)]).T
c = []

for i in range(1,6):
    r = np.dot(A,r)
    print(f"This iteration{i},new Page Rank is:\n{r}")
