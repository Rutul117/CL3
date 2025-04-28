import numpy as np

# Universe of Discourse
U = [0, 1, 2, 3, 4, 5]

# Fuzzy sets with membership values
A = {0: 0.1, 1: 0.5, 2: 0.8, 3: 1.0, 4: 0.6, 5: 0.2}
B = {0: 0.3, 1: 0.7, 2: 0.4, 3: 0.9, 4: 0.5, 5: 0.1}

# Union: max(A(x), B(x))
def union(a, b):
    return {x: max(a[x], b[x]) for x in a}
    # result = {}
    #     for x in a:
    #         result[x] = max(a[x], b[x])
    #     return result

# Intersection: min(A(x), B(x))
def intersection(a, b):
    return {x: min(a[x], b[x]) for x in a}

# Complement: 1 - A(x)
def complement(a):
    return {x: round(1 - a[x], 2) for x in a}

# Difference: max(A(x), 1 - B(x))
def difference(a, b):
    return {x: max(a[x], 1 - b[x]) for x in a}

# Cartesian Product: μR(u,v) = min(μA(u), μB(v))
def cartesian_product(a, b):
    return {(u, v): min(a[u], b[v]) for u in a for v in b}

# Max-Min Composition: μT(u, w) = max[min(μR(u,v), μS(v,w)) for v]
def max_min_composition(R, S, U, V, W):
    T = {}
    for u in U:
        for w in W:
            values = []
            for v in V:
                r = R.get((u, v), 0)
                s = S.get((v, w), 0)
                values.append(min(r, s))
            T[(u, w)] = max(values)
    return T

# Demo output
print("Set A:", A)
print("Set B:", B)
print("\nUnion:", union(A, B))
print("Intersection:", intersection(A, B))
print("Complement of A:", complement(A))
print("Difference A \\ B:", difference(A, B))

# Cartesian Product
R = cartesian_product(A, B)
print("\nFuzzy Relation R (A × B):")
for key, val in R.items():
    print(f"{key}: {val}")

# Create another fuzzy set C to form S
C = {0: 0.4, 1: 0.6, 2: 0.9, 3: 0.3, 4: 0.5, 5: 0.2}
S = cartesian_product(B, C)

# Max-Min Composition
T = max_min_composition(R, S, U, U, U)
print("\nMax-Min Composition (R ○ S):")
for key, val in T.items():
    print(f"{key}: {round(val, 2)}")
