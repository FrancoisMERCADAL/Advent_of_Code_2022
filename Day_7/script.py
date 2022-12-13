from class_directory import *

FILE_NAME = "logs.txt"
FILESYSTEM_TOTAL_SPACE = 70000000
MAX_DIRECTORY_SIZE = 100000
UPDATE_SIZE = 30000000

def print_filesystem(current_directory, i):
    offset = '   ' * i
    print(current_directory.display_directory(offset))
    for directory in current_directory.connected_directories:
        print_filesystem(directory, i+1)
        
    return None

def add_size_to_filesystem(current_directory, value):
    while current_directory.parent_directory != None:
        current_directory = current_directory.parent_directory
        current_directory.size += value

def build_file_system(file, current_directory):
    try:
        line = file.readline().split()
        if line[0] == "$" and line[1] == "cd":
            if line[2] == "/":
                while current_directory.parent_directory != None:
                    current_directory = current_directory.parent_directory
            elif line[2] == "..":
                current_directory = current_directory.parent_directory
            else:
                new_directory = Directory(line[2], 0, current_directory, [])
                current_directory.connected_directories.append(new_directory)
                build_file_system(file, new_directory)
        elif line[0] != "dir" and line[0] != "$":
            current_directory.size += int(line[0])
            if current_directory.parent_directory != None:
                add_size_to_filesystem(current_directory, int(line[0]))
        build_file_system(file, current_directory)
    except:
        pass

# PART 1
def get_directories_under_max_size(filesystem, array):
    if filesystem.size <= MAX_DIRECTORY_SIZE:
        array.append(filesystem.size)
    for directory in filesystem.connected_directories:
        get_directories_under_max_size(directory, array)

def get_sum_dir_under_max(file):
    filesystem = Directory("/", 0, None, [])
    file.readline()

    build_file_system(file, filesystem)

    array = []
    get_directories_under_max_size(filesystem, array)
    return sum(array)

def no_space_left_on_device_part1():
    file = open(FILE_NAME, "r")
    sum_dir = get_sum_dir_under_max(file)
    file.close()
    return sum_dir

# PART 2
def get_directories_to_delete(directory, space_to_delete, array):
    if directory.size >= space_to_delete:
        array.append(directory.size)
    for dir in directory.connected_directories:
        get_directories_to_delete(dir, space_to_delete, array)

def get_min_directory_to_delete(file):
    filesystem = Directory("/", 0, None, [])
    file.readline()
    build_file_system(file, filesystem)

    unused_space = FILESYSTEM_TOTAL_SPACE - filesystem.size
    space_to_delete = UPDATE_SIZE - unused_space

    array = []
    get_directories_to_delete(filesystem, space_to_delete, array)
    return min(array)

def no_space_left_on_device_part2():
    file = open(FILE_NAME, "r")
    min_directory = get_min_directory_to_delete(file)
    file.close()
    return min_directory

### TEST AREA
# Part 1
#print(no_space_left_on_device_part1())
# Output: 1182909

# Part 2
#print(no_space_left_on_device_part2())
# Output: 2832508
