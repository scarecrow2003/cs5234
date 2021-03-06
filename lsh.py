import sys
import numpy as np

input_lines = sys.stdin.readlines()
n, d, t = tuple([int(s) for s in input_lines[0].split(' ')])

P = []
Q = []

for i in range(1, n + 1):
    point = [int(s) for s in input_lines[i].rstrip('\n').split()]
    P.append(point)

for i in range(n + 1, n + t + 1):
    point = [int(s) for s in input_lines[i].rstrip('\n').split()]
    Q.append(point)

# Now, P will give the list of set points and Q will give the list of query points

# P and Q can be converted to numpy arrays etc. as required 

# Code for ann algorithm populating ann[]

P = np.asarray(P)
Q = np.asarray(Q)

l = 20
k = 10
h = [np.random.choice(d, k, replace=False) for _ in range(l)]
T = []
for i in range(l):
    T.append({})

# Preprocessing
for i in range(n):
    x = P[i]
    for j in range(l):
        key = tuple(x[h[j]])
        val = T[j].get(key)
        if val == None:
            T[j][key] = [i]
        else:
            val.append(i)

# Query
ann = []
for i in range(t):
    num = 0
    y = Q[i]
    result = 'OUT'
    for j in range(l):
        key = tuple(y[h[j]])
        val = T[j].get(key)
        if val != None:
            for idx in val:
                if np.sum(P[idx] != y) <= 20:
                    result = idx
                else:
                    num += 1
                    if num > 10*l:
                        break
        if num > 10*l:
            break
    ann.append(result)

# use brute force to check, the above algorithm only has one query that is different from the actual result.
# real = []
# for i in range(t):
#     y = Q[i]
#     min = 100
#     index = -1
#     for j in range(n):
#         dis = np.sum(y != P[j])
#         if dis < min:
#             min = dis
#             index = j
#     real.append(index)
# print("number of result that is different from the actual result: ")
# print(np.sum(ann != real))

# print("first 50 results:")
# for i in range(50):
#    print(ann[i])

for i in range(t):
    print(ann[i])