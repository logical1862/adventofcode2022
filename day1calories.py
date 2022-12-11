#find elf with highest calories, return calorie count

filepath = "AdventOfCode2022\elvescalories.txt"

highestCalories = []

CurrentElfCount = 0
with open(filepath, "rt", encoding="utf-8") as inputFile:
    for line in inputFile.readlines():
        if line == "\n":
            highestCalories.append(CurrentElfCount)
            CurrentElfCount = 0
        else:
            CurrentElfCount += int(line)

# -----part one solution
# print(max(highestCalories))

# -----part 2 solution
highestCalories.sort(reverse=True)
TopThreeElves = highestCalories[:3]
print(TopThreeElves)
ThreeCount = 0
for num in TopThreeElves:
    ThreeCount += num
print(ThreeCount)