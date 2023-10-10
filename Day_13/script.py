from ast import literal_eval

FILE_NAME = "distress_signal.txt"

def Compare(arr1, arr2, index, sum):
    if type(arr1[index]) == type(list) and type(arr2[index]) == type(list):
        Compare(arr1[index], arr2[index], 0, sum)
    return 0

with open(FILE_NAME) as f:
    content = [tuple(map(literal_eval, x)) for x in [a.split() for a in f.read().split("\n\n")]]

print(content[1][0])
print(type(content[1][0]))

indice_sum = 0

for i in range(len(content)):
    arr1 = content[i][0]
    arr2 = content[i][1]

    #indice_sum += Compare(arr1, arr2, 0, 0)

print(arr2)
