FILE_NAME = "rope_movements.txt"

# PART 1
def is_tail_move(head_position, tail_position):
    # Same line
    if head_position[0] == tail_position[0]:
        if abs(head_position[1] - tail_position[1]) > 1:
            return True
    # Same column
    elif head_position[1] == tail_position[1]:
        if abs(head_position[0] - tail_position[0]) > 1:
            return True
    # Diagonal position
    elif abs(head_position[0] - tail_position[0]) > 1 or abs(head_position[1] - tail_position[1]) > 1:
        return True
    return False

def get_tail_positions(file):
    head_position = [0,0]
    tail_position = [0,0]
    tail_position_visited = []
    for line in file:
        line_arr = line.split()
        letter = line_arr[0]
        nb = int(line_arr[1])
        for i in range(0, nb):
            if letter == "R":
                head_position[0] += 1
            elif letter == "L":
                head_position[0] -= 1
            elif letter == "U":
                head_position[1] += 1
            elif letter == "D":
                head_position[1] -= 1
            if is_tail_move(head_position, tail_position):
                if letter == "R":
                    tail_position = [head_position[0] - 1, head_position[1]]
                elif letter == "L":
                    tail_position = [head_position[0] + 1, head_position[1]]
                elif letter == "U":
                    tail_position = [head_position[0], head_position[1] - 1]
                elif letter == "D":
                    tail_position = [head_position[0], head_position[1] + 1]
            if (tail_position[0], tail_position[1]) not in tail_position_visited:
                tail_position_visited.append((tail_position[0], tail_position[1]))
    return len(tail_position_visited)

def rope_bridge_part1():
    file = open(FILE_NAME, "r")
    count = get_tail_positions(file)
    file.close()
    return count

# PART 2
rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
tail9_positions_visited = []
file = open(FILE_NAME, "r")
for line in file:
    line_arr = line.split()
    letter = line_arr[0]
    nb = int(line_arr[1])
    for i in range(0, nb):
        previous_rope_positions = [rope[0][:], rope[1][:], rope[2][:], rope[3][:], rope[4][:], rope[5][:], rope[6][:], rope[7][:], rope[8][:],rope[9][:]]
        if letter == "R":
            rope[0][0] += 1
        elif letter == "L":
            rope[0][0] -= 1
        elif letter == "U":
            rope[0][1] += 1
        elif letter == "D":
            rope[0][1] -= 1
        for k in range(1,len(rope)):
            if is_tail_move(rope[k-1], rope[k]):
                if letter == "R":
                    rope[k] = [rope[k-1][0] - 1, rope[k-1][1]]
                elif letter == "L":
                    rope[k] = [rope[k-1][0] + 1, rope[k-1][1]]
                elif letter == "U":
                    rope[k] = [rope[k-1][0], rope[k-1][1] - 1]
                elif letter == "D":
                    rope[k] = [rope[k-1][0], rope[k-1][1] + 1]
                if is_tail_move(rope[k], previous_rope_positions[k]):
                    rope[k] = previous_rope_positions[k-1]
            else:
                break
        print("Rope positions: ", rope)
        if (rope[9][0], rope[9][1]) not in tail9_positions_visited:
            tail9_positions_visited.append((rope[9][0], rope[9][1]))
file.close()
print(len(tail9_positions_visited))

### TEST AREA
# Part 1
#print(rope_bridge_part1())
# Output: 5930

# Part 2
#print(())
# Output: 

