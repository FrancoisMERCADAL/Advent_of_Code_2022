FILE_NAME = "rucksacks_items.txt"

def get_priority_object(char):
    if ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38

# Part 1
def get_count_rucksack_reorganization(file):
    count = 0
    for line in file:
        line = list(line)
        part1 = line[:int(len(line)/2)]
        part2 = line[int(len(line)/2):]
        for letter in part1:
            if letter in part2:
                count += get_priority_object(letter)
                break
    return count

def rucksack_reorganization_part1():
    file = open(FILE_NAME, "r")
    count = get_count_rucksack_reorganization(file)
    file.close()
    return count

# Part 2
def get_count_badges(file):
    count = 0
    array = []
    for line in file:
        array.append(list(line))
        if len(array) == 3:
            for letter in array[0]:
                if letter in array[1] and letter in array[2]:
                    count += get_priority_object(letter)
                    array = []
                    break
    return count

def rucksack_reorganization_part2():
    file = open(FILE_NAME, "r")
    count = get_count_badges(file)
    file.close()
    return count

### TEST AREA
# Part 1
#print(rucksack_reorganization_part1())
# Output: 8202

# Part 2
#print(rucksack_reorganization_part2())
# Output: 2864



