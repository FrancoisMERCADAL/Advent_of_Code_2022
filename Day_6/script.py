FILE_NAME = "buffer.txt"

# PART 1
PACKET_LENGTH = 4

def get_marker_position(file):
    line = list(file.readline())
    for i in range(len(line) - PACKET_LENGTH):
        arr = [line[i], line[i+1], line[i+2], line[i+3]]
        if len(set(arr)) == len(arr):
            return i+4
    
def tuning_trouble_part1():
    file = open(FILE_NAME, "r")
    marker_position = get_marker_position(file)
    file.close()
    return marker_position

# PART 2
MESSAGE_LENGTH = 14

def get_message_position(file):
    line = list(file.readline())
    for i in range(len(line) - MESSAGE_LENGTH):
        arr = [line[i+k] for k in range(0,MESSAGE_LENGTH)]
        if len(set(arr)) == len(arr):
            return i+14

def tuning_trouble_part2():
    file = open(FILE_NAME, "r")
    message_position = get_message_position(file)
    file.close()
    return message_position

### TEST AREA
# Part 1
#print(tuning_trouble_part1())
# Output: 1155

# Part 2
#print(tuning_trouble_part2())
# Output: 2789
