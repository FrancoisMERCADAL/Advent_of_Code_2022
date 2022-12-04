FILE_NAME = "pairs_assignments.txt"

# Part 1
def get_count_overlaps(file):
    count = 0
    for line in file:
        line = line.split(',')
        range1 = list(map(int, line[0].split('-')))
        range2 = list(map(int, line[1].replace('\n', '').split('-')))
        if (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range2[0] >= range1[0] and range2[1] <= range1[1]):
            count += 1
    return count

def camp_cleanup_part1():
    file = open(FILE_NAME, "r")
    count = get_count_overlaps(file)
    file.close()
    return count

# Part 2
def common_element(list1,list2):
    for nb in list1:
        if nb in list2:
            return True
    return False

def count_common_tasks_presences(file):
    count = 0
    for line in file:
        line = line.split(',')
        range1 = list(map(int, line[0].split('-')))
        range2 = list(map(int, line[1].replace('\n', '').split('-')))
        range1 = list(range(range1[0],range1[1]+1))
        range2 = list(range(range2[0],range2[1]+1))
        if common_element(range1,range2):
            count += 1
    return count

def camp_cleanup_part2():
    file = open(FILE_NAME, "r")
    count = count_common_tasks_presences(file)
    file.close()
    return count

### TEST AREA
# Part 1
#print(camp_cleanup_part1())
# Output: 490

# Part 2
#print(camp_cleanup_part2())
# Output: 921
