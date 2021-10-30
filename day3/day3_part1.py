with open("input_trees.txt") as file:
    map = file.readlines()
    map = [ line.strip() for line in map ]

numOfTrees = 0
row, column = 0, 0

while row + 1 < len(map):
    row += 1
    column += 3

    space = map[row][column % len(map[row])]
    if space == "#":
        numOfTrees += 1

print(numOfTrees)
