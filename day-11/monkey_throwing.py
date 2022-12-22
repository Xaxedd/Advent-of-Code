from dataclasses import dataclass
from enum import Enum
from math import floor
from typing import List


class PART(Enum):
    ONE = 0
    TWO = 1


def str_to_int(x):
    return int(x)


def get_monkey_list(puzzle_input):
    monkey_list = []
    for line in puzzle_input:
        line = line.strip()
        if "Monkey" in line:
            monkey = []
        elif "Starting items:" in line:
            line = line.replace("Starting items: ", "")
            line = line.split(", ")
            line = list(map(str_to_int, line))
            monkey.append(line)
        elif "Operation" in line:
            line = line.replace("Operation: new = ", "")
            line = eval("lambda old:" + line)
            monkey.append(line)
        elif "Test" in line:
            line = line.replace("Test: divisible by ", "")
            monkey.append(int(line))
        elif "If true" in line:
            line = line.replace("If true: throw to monkey ", "")
            monkey.append(int(line))
        elif "If false" in line:
            line = line.replace("If false: throw to monkey ", "")
            monkey.append(int(line))
            monkey.append(0)
            monkey_list.append(monkey)
    return monkey_list


def get_answer(part: PART):
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()
    monkey_list = get_monkey_list(puzzle_input)

    if part is PART.ONE:
        rounds = 20
    if part is PART.TWO:
        rounds = 10000
        super_modulo = 1
        for monkey in monkey_list:
            super_modulo *= monkey[2]

    for i in range(rounds):
        for monkey in monkey_list:
            for item in monkey[0]:
                item_score = monkey[1](item)
                if part is PART.ONE:
                    item_score = floor(item_score / 3)
                elif part is PART.TWO:
                    item_score = item_score % super_modulo
                if item_score % monkey[2] == 0:
                    monkey_list[monkey[3]][0].append(item_score)
                else:
                    monkey_list[monkey[4]][0].append(item_score)
                monkey[5] += 1
            monkey[0] = []

    sorted_list = sorted(monkey_list, key=lambda x: x[5])
    return sorted_list[-1][5] * sorted_list[-2][5]


print("part one answer:", get_answer(PART.ONE))
print("part two answer:", get_answer(PART.TWO))
