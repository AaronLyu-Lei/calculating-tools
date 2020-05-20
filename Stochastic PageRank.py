import numpy as np

A = np.matrix([(0,0,0,0.5),(0.5,0,0.5,0.5),(0,1,0,0),(0.5,0,0.5,0)])
r = np.matrix([(0.25,0.25,0.25,0.25)]).T
v = np.matrix([(0.25,0.25,0.25,0.25)]).T
c = []
i = 1
#input your beta
beta =0.8

while True:
    c.append(r)
    x = beta*A
    y = (1-beta)*v
    r = np.around(np.dot(x,r) + y,3)
    if (r == c[-1]).all():
        break
    print(f"This iteration{i},new Page Rank is :\n{r}")
    i += 1
