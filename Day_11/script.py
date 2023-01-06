from monkey import *

FILE_NAME = "monkeys.txt"
NB_ROUNDS_PART1 = 20
NB_ROUNDS_PART2 = 10000

def parse_file(file):
    monkeys = []
    for line in file:
        line = line.split()
        if line[0] == "Monkey":
            line = file.readline()
            items = list(map(int, line.split(":")[1].replace(" ", "").replace("\n","").split(",")))

            line = file.readline()
            operation = line.split("=")[1].replace(" ", "").replace("old", "").replace("\n", "")
            if len(operation) == 1:
                if operation == "*":
                    operation = ["*", "itself"]
                else:
                    operation = ["+", "itself"]
            else:
                if operation[0] == "*":
                    operation = ["*", int(operation[1:])]
                else:
                    operation = ["+", int(operation[1:])]

            line = file.readline()
            divide_test = int(line.split()[3])

            line = file.readline()
            divide_test_true_case = int(line.split()[-1])

            line = file.readline()
            divide_test_false_case = int(line.split()[-1])

            monkeys.append(Monkey(items, operation, divide_test, divide_test_true_case, divide_test_false_case))
            file.readline()
    return monkeys

def calculate_monkey_business(monkeys):
    array_inspections = [monkeys[i].inspected_items for i in range(len(monkeys))]
    array_inspections.sort()
    return array_inspections[-1] * array_inspections[-2]

# PART 1
def get_monkey_business_part1(file, nb_rounds):
    round = 0
    monkeys = parse_file(file)
    while round != nb_rounds:
        round += 1
        for i in range(len(monkeys)):
            monkeys[i].inspect_items_part1()
            for item in monkeys[i].items:
                if monkeys[i].perform_division_test(item) == True:
                    monkeys[monkeys[i].divide_test_true_case].items.append(item)
                else:
                    monkeys[monkeys[i].divide_test_false_case].items.append(item)
            monkeys[i].items = []
    return calculate_monkey_business(monkeys)

def monkey_in_the_middle_part1():
    file = open(FILE_NAME, "r")
    monkey_business = get_monkey_business_part1(file, NB_ROUNDS_PART1)
    file.close()
    return monkey_business

# PART 2
def calculate_supermodulo(monkeys):
    supermodulo = 1
    for monkey in monkeys:
        supermodulo *= monkey.divide_test
    return supermodulo

def get_monkey_business_part2(file, nb_rounds):
    round = 0
    file = open(FILE_NAME, "r")
    monkeys = parse_file(file)
    file.close()

    supermodulo = calculate_supermodulo(monkeys)

    while round != nb_rounds:
        round += 1
        for i in range(len(monkeys)):
            monkeys[i].inspect_items_part2(supermodulo)
            for item in monkeys[i].items:
                if monkeys[i].perform_division_test(item) == True:
                    monkeys[monkeys[i].divide_test_true_case].items.append(item)
                else:
                    monkeys[monkeys[i].divide_test_false_case].items.append(item)
            monkeys[i].items = []
    return calculate_monkey_business(monkeys)

def monkey_in_the_middle_part2():
    file = open(FILE_NAME, "r")
    monkey_business = get_monkey_business_part2(file, NB_ROUNDS_PART2)
    file.close()
    return monkey_business

### TEST AREA
# Part 1
#print(monkey_in_the_middle_part1())
# Output: 117640

# Part 2
#print(monkey_in_the_middle_part2())
# Output: 30616425600
