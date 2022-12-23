class Monkey:
    def __init__(self, items, operation, divide_test, divide_test_true_case, divide_test_false_case):
        self.items = items
        self.operation = operation 
        self.divide_test = divide_test
        self.divide_test_true_case = divide_test_true_case
        self.divide_test_false_case = divide_test_false_case
        self.inspected_items = 0

    def inspect_items_part1(self):
        for i in range(len(self.items)):
            if self.operation[0] == "*" and self.operation[1] == "itself":
                self.items[i] = int(self.items[i] * self.items[i] / 3)
            elif self.operation[0] == "*":
                self.items[i] = int(self.items[i] * self.operation[1] / 3)
            elif self.operation[0] == "+" and self.operation[1] == "itself":
                self.items[i] = int((self.items[i] + self.items[i])/3)
            elif self.operation[0] == "+":
                self.items[i] = int((self.items[i] + self.operation[1])/3)
        self.inspected_items += len(self.items)

    def inspect_items_part2(self):
        for i in range(len(self.items)):
            if self.operation[0] == "*" and self.operation[1] == "itself":
                self.items[i] = self.items[i] * self.items[i]
            elif self.operation[0] == "*":
                self.items[i] = self.items[i] * self.operation[1]
            elif self.operation[0] == "+" and self.operation[1] == "itself":
                self.items[i] = self.items[i] + self.items[i]
            elif self.operation[0] == "+":
                self.items[i] = self.items[i] + self.operation[1]
        self.inspected_items += len(self.items)

    def perform_division_test(self, item):
        if item % self.divide_test == 0:
            return True
        return False
    
    def toString(self):
        return "Items: " + str(self.items).strip('[]') + "\noperation: " + str(self.operation).strip('[]') + "\ndivide test: " + str(self.divide_test) + "\ntest true case: " + str(self.divide_test_true_case) + "\ntest false case: " + str(self.divide_test_false_case) + "\ninspected objects: " + str(self.inspected_items)

    
