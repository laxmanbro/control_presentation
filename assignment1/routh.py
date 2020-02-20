import numpy as np
import itertools
n = int(input("degree "))
c = np.zeros(100)
for i in range(0, n+1):
    c[i] = int(input())

d = np.zeros([n+1, n+1])
for j in range(0, n-1):
    d[0, j] = c[2*j]
    d[1, j] = c[(2*j)+1]


for i in range(2, n+1):
    for j in range(0, n-1):
        d[i, j] = (((d[i-1, 0]*d[i-2, j+1]) -
                    (d[i-1, j+1]*d[i-2, 0]))/(d[i-1, 0]))
    if(d[i, 0] == 0):
        d[i, 0] = 0.00001

print(d)
x = []
for i in range(0, n+1):
    x.append(d[i, 0])

k = (len(list(itertools.groupby(x, lambda x: x > 0)))-1)


# Printing answer
# print(ans)


if k == 0:
    print("no sign chages")
else:
    print("no of sign chages is : ", k)
