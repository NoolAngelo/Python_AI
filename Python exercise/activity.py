# Define the sets
B = {1, 3, 5}
E = {2, 3, 5, 6}
T = {4, 2, 9, 6}
H = {2, 9, 3, 0}

# Perform the operations
B_union_H = B.union(H)
E_intersect_T = E.intersection(T)
B_union_E_union_T = B.union(E, T)
H_diff_E = H.difference(E)
B_diff_E_union_T = B.difference(E).union(T)

# Print the results
print("B union H:", B_union_H)
print("E intersect T:", E_intersect_T)
print("B union E union T:", B_union_E_union_T)
print("H - E:", H_diff_E)
print("B - E union T:", B_diff_E_union_T)