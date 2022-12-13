FILE_NAME = "map.txt"

# PART 1
def is_tree_visible(forest, i, k):
    if max(forest[i][0:k]) < forest[i][k] or max(forest[i][k+1:]) < forest[i][k] :
        return 1
    tree_column = [forest[line_nb][k] for line_nb in range(len(forest))]
    if max(tree_column[0:i]) < forest[i][k] or max(tree_column[i+1:]) < forest[i][k]:
        return 1
    return 0

def nb_visible_trees(file):
    forest = []
    visible_trees = 0
    for line in file:
        forest.append(list(map(int, line.replace("\n", ""))))
    
    for i in range(len(forest)):
        for k in range(len(forest[i])):
            if i == 0 or i == len(forest) - 1 or k == 0 or k == len(forest[i]) - 1:
                visible_trees += 1
            else:
                if is_tree_visible(forest, i, k):
                    visible_trees += 1
    return visible_trees

def treetop_treehouse_part1():
    file = open(FILE_NAME, "r")
    visible_trees = nb_visible_trees(file)
    file.close()
    return visible_trees

# PART 2
def calculate_scenic_score(forest, i, k):
    west_side = forest[i][0:k]
    west_count = 0
    east_side = forest[i][k+1:]
    east_count = 0
    tree_column = [forest[line_nb][k] for line_nb in range(len(forest))]
    north_side = tree_column[0:i]
    north_count = 0
    south_side = tree_column[i+1:]
    south_count = 0

    ## WEST
    for index in range(len(west_side[::-1])):
        west_count += 1
        if west_side[::-1][index] >= forest[i][k]:
            break
    
    ## EAST
    for index in range(len(east_side)):
        east_count += 1
        if east_side[index] >= forest[i][k]:
            break

    ## NORTH
    for index in range(len(north_side[::-1])):
        north_count += 1
        if north_side[::-1][index] >= forest[i][k]:
            break

    ## SOUTH
    for index in range(len(south_side)):
        south_count += 1
        if south_side[index] >= forest[i][k]:
            break
    return west_count * east_count * north_count * south_count

def get_max_scenic_score(file):
    forest = []
    max_scenic_score = 0
    for line in file:
        forest.append(list(map(int, line.replace("\n", ""))))

    for i in range(len(forest)):
        for k in range(len(forest[i])):
            if i == 0 or i == len(forest) - 1 or k == 0 or k == len(forest[i]) - 1:
                pass
            else:
                scenic_score = calculate_scenic_score(forest, i, k)
                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score
    return max_scenic_score

def treetop_treehouse_part2():
    file = open(FILE_NAME, "r")
    max_scenic_score = get_max_scenic_score(file)
    file.close()
    return max_scenic_score

### TEST AREA
# Part 1
#print(treetop_treehouse_part1())
# Output: 1669

# Part 2
#print(treetop_treehouse_part2())
# Output: 331344
