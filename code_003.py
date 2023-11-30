


# reading the textfile to "buffer"
with open("/home/tex/VSCode/Python/adventofcode/2022/01/input", "r") as f:
    buffer = f.read()

length = len(buffer)

#getting the length of "numOfElves"
double_new_lines = 0
for i in range(length-1):
    if ord(buffer[i]) == ord(buffer[i+1]) == 10:
        double_new_lines += 1



numOfElves = [0] * double_new_lines

#setup for re-looping to get the elves calorie-numbers
elve_index = 0
number_total = 0
number_for_calculation = 0
for i in range(length-1):
    if ord(buffer[i]) == 10 and ord(buffer[i+1]) == 10:
        numOfElves[elve_index] = number_total + number_for_calculation
        elve_index += 1
        number_total = 0
        number_for_calculation = 0
    if ord(buffer[i]) != 10:
        number_for_calculation = number_for_calculation * 10
        number_for_calculation = number_for_calculation + ord(buffer[i]) - 48
    if ord(buffer[i]) == 10:
        number_total += number_for_calculation
        number_for_calculation = 0
print(max(numOfElves))
print(numOfElves)
