with open("input_trees.txt") as file:
    map = file.readlines()
    map = [ line.strip() for line in map ]

slopes = [(1,1), (3,1), (5,1), (7,1),(1,2)]

total = 1

for slope in slopes:
    treeCount = 0
    row, column = 0, 0

    while row + 1 < len(map):
        row += slope[1]
        column += slope[0]

        space = map[row][column % len(map[row])]
        if space == "#":
            treeCount += 1

    total *= treeCount

print(total)
