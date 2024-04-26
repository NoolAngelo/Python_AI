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
# Additional operations
E_diff_B = E.difference(B)
T_intersect_H = T.intersection(H)

# Print the results
print("E - B:", E_diff_B)
print("T intersect H:", T_intersect_H)

# Print the results
print("B union H:", B_union_H)
print("E intersect T:", E_intersect_T)
print("B union E union T:", B_union_E_union_T)
print("H - E:", H_diff_E)
print("B - E union T:", B_diff_E_union_T)
print("E - B:", E_diff_B)
print("T intersect H:", T_intersect_H)
