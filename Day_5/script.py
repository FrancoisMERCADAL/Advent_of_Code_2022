from collections import OrderedDict

FILE_NAME = "cargo_crane.txt"

def read_header_line(cargo_crane, line):
    count = 1
    for i in range(1,len(line),4):
        if line[i] != ' ':
            if count in cargo_crane:
                cargo_crane[count].append(line[i])
            else:
                cargo_crane[count] = [line[i]]
        count += 1
    return cargo_crane

# PART 1
def get_top_crates_initials(file):
    flag = False
    cargo_crane = {}
    for line in file:
        if line == " 1   2   3   4   5   6   7   8   9 \n":
            file.readline()
            flag = True
        if flag == False:
            cargo_crane = read_header_line(cargo_crane, line)
        if flag == True and line != " 1   2   3   4   5   6   7   8   9 \n":
            array = line.split()
            nb = int(array[1])
            start = int(array[3])
            destination = int(array[5])
            for i in range(nb):
                cargo_crane[destination].insert(0, cargo_crane[start][0])
                cargo_crane[start].pop(0)
            continue
    cargo_crane = OrderedDict(sorted(cargo_crane.items()))
    arr = []
    for val in cargo_crane.values():
        arr.append(val[0])
    return ''.join(arr)

def supply_stacks_part1():
    file = open(FILE_NAME, "r")
    initials = get_top_crates_initials(file)
    file.close()
    return initials

# PART 2
def get_top_crates_initials2(file):
    flag = False
    cargo_crane = {}
    for line in file:
        if line == " 1   2   3   4   5   6   7   8   9 \n":
            file.readline()
            flag = True
        if flag == False:
            cargo_crane = read_header_line(cargo_crane, line)
        if flag == True and line != " 1   2   3   4   5   6   7   8   9 \n":
            array = line.split()
            nb = int(array[1])
            start = int(array[3])
            destination = int(array[5])
            for i in range(0,nb):
                cargo_crane[destination].insert(0, cargo_crane[start][nb-1-i])
            del cargo_crane[start][0:nb]
    
    cargo_crane = OrderedDict(sorted(cargo_crane.items()))
    arr = []
    for val in cargo_crane.values():
        arr.append(val[0])
    return(''.join(arr))

def supply_stacks_part2():
    file = open(FILE_NAME, "r")
    initials = get_top_crates_initials2(file)
    file.close()    
    return initials

### TEST AREA
# Part 1
#print(supply_stacks_part1())
# Output: RFFFWBPNS

# Part 2
#print(supply_stacks_part2())
# Output: CQQBBJFCS
