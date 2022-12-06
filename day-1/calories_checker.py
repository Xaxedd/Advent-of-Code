elves_list = []
elves_calories = open("calories_of_elves.txt", "r", encoding="utf8").readlines()

sum_of_calories = 0
for line in elves_calories:
    line = line.strip()
    if line != "":
        sum_of_calories += int(line)
    else:
        elves_list.append(sum_of_calories)
        sum_of_calories = 0
elves_list.sort()
print("part one answer:", elves_list[-1])
print("part two answer:", elves_list[-1] + elves_list[-2] + elves_list[-3])