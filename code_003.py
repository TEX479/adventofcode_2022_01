


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
caloriesTotal = 0
caloriesInProgress = 0
#loop to fill the "numOfElves" array
for i in range(length-1):
    #if there is a new elve incoming, add the calorieTotal to the current numOfElves[i]
    if ord(buffer[i]) == 10 and ord(buffer[i+1]) == 10:
        numOfElves[elve_index] = caloriesTotal + caloriesInProgress
        elve_index += 1
        caloriesTotal = 0
        caloriesInProgress = 0
    #if there is not a new line, add the char to the caloriesInProgress (to get the int of a multi-charred value)
    #this effectively adds the single chars together to the decimal number
    if ord(buffer[i]) != 10:
        caloriesInProgress = caloriesInProgress * 10
        caloriesInProgress = caloriesInProgress + ord(buffer[i]) - 48
    #if there is a new line, add the calculated decimal to the current elves total
    if ord(buffer[i]) == 10:
        caloriesTotal += caloriesInProgress
        caloriesInProgress = 0

print(max(numOfElves))
print(numOfElves)
