FILE_NAME = "hill.txt"

def separate_chars_and_convert_to_number(input_string):
    input_string = [*input_string]
    print(input_string)
    output = []
    for char in input_string:
        if char.islower():
            output.append(int(ord(char) - 96))
        elif char == '\n':
            continue
        else:
            output.append(char)
    return output

def get_S_and_E_position(hill):
    pos_E = None
    pos_S = None
    for i in range(len(hill)):
        if 'E' in hill[i]:
            pos_E = (i, hill[i].index('E'))
        if 'S' in hill[i]:
            pos_S = (i, hill[i].index('S'))
    return pos_E, pos_S

hill = []
line_nb = 0

file = open(FILE_NAME, "r")
for line in file:
    hill.append(separate_chars_and_convert_to_number(line))
file.close()

pos_E, pos_S = get_S_and_E_position(hill)
