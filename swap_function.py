def swap_values(L, index1, index2):
    temporary = L[index1]
    L[index1] = L[index2]
    L[index2] = temporary
    return L

L = [2,3,6,7]
L2 = swap_values(L, 1, 3)
print(L2)