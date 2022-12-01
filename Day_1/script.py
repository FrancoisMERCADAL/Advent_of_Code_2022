FILE_NAME = "elves_supplies.txt"

# Part 1
def get_max_cal_count(file):
    sum_supplies = []
    elve_supplies = []

    for line in file:
        try:
            elve_supplies.append(int(line))
        except:
            sum_supplies.append(sum(elve_supplies))
            elve_supplies = []
    return max(sum_supplies)

def calorie_counting_part1():
    file = open(FILE_NAME, "r")
    max_cal = get_max_cal_count(file)
    file.close()
    return max_cal

# Part 2
def get_sum_top3_max_cal_count(file):
    elve_supplies = []
    max_cal = 0
    second_max_cal = 0
    third_max_cal = 0

    for line in file:
        try:
            elve_supplies.append(int(line))
        except:
            elve_sum = sum(elve_supplies)
            if elve_sum > max_cal:
                third_max_cal = second_max_cal
                second_max_cal = max_cal
                max_cal = elve_sum
            elif elve_sum > second_max_cal:
                third_max_cal = second_max_cal
                second_max_cal = elve_sum
            elif elve_sum > third_max_cal:
                third_max_cal = elve_sum
            elve_supplies = []
    return sum([max_cal,second_max_cal,third_max_cal])

def calorie_counting_part2():
    file = open(FILE_NAME, "r")
    sum_top3 = get_sum_top3_max_cal_count(file)
    file.close()
    return sum_top3

### TEST AREA
# Part 1
#print(calorie_counting_part1())
# Output: 69883

# Part 2
#print(calorie_counting_part2())
# Output: 207576
