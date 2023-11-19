cell = (4, 5)
neighboring_cells = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if (i, j) != (0, 0):
            neighboring_cells.append((cell[0]+i, cell[1]+j))
            
# for flanders in neighboring_cells:
#   print(flanders)
print(neighboring_cells)

# print((4,5) == (4,5))