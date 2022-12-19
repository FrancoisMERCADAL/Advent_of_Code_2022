FILE_NAME = "signal.txt"

# PART 1
def sum_signal_strengths(cycle_nb, interest_cycles, X, sum_signal_strenghs):
    if cycle_nb in interest_cycles:
        sum_signal_strenghs += X * cycle_nb
    return sum_signal_strenghs

def get_sum_signal_strengths(file):
    X = 1
    cycle_nb = 0
    interest_cycles = [20, 60, 100, 140, 180, 220]
    sum_signal_strenghs = 0
    for line in file:
        cycle_nb += 1
        sum_signal_strenghs = sum_signal_strengths(cycle_nb, interest_cycles, X, sum_signal_strenghs)
        line = line.split()
        if line[0] == "noop":
            pass
        elif line[0] == "addx":
            nb = int(line[1])
            cycle_nb += 1
            sum_signal_strenghs = sum_signal_strengths(cycle_nb, interest_cycles, X, sum_signal_strenghs)
            X += nb
    return sum_signal_strenghs

def cathode_ray_tube_part1():
    file = open(FILE_NAME, "r")
    sum_signal_strengths = get_sum_signal_strengths(file)
    file.close()
    return sum_signal_strengths

# PART 2
def get_char_to_append(position_pixel_draw, sprite_middle_position):
    if position_pixel_draw in [sprite_middle_position-1, sprite_middle_position, sprite_middle_position+1]:
        return "#"
    else:
        return "."

def display_screen(output):
    for array in output:
        print(''.join(array))
    return None

def get_screen_displayed_letters(file):
    screen_width = 40
    screen_height = 6
    position_pixel_draw = 0
    sprite_middle_position = 1
    
    output = [[] for i in range(screen_height)]
    current_height = 0
    for line in file:
        line = line.split()
        output[current_height].append(get_char_to_append(position_pixel_draw, sprite_middle_position))
        if line[0] == "addx":
            position_pixel_draw += 1
            if position_pixel_draw >= screen_width:
                position_pixel_draw -= screen_width
                current_height += 1
            output[current_height].append(get_char_to_append(position_pixel_draw, sprite_middle_position))
            nb = int(line[1])
            sprite_middle_position += nb
        position_pixel_draw += 1
        if position_pixel_draw >= screen_width:
            position_pixel_draw -= screen_width
            current_height += 1
    display_screen(output)

def cathode_ray_tube_part2():
    file = open(FILE_NAME, "r")
    get_screen_displayed_letters(file)
    file.close()
    return "Screen displayed above"

### TEST AREA
# Part 1
#print(cathode_ray_tube_part1())
# Output: 17180

# Part 2
#print(cathode_ray_tube_part2())
# Output: REHPRLUB
