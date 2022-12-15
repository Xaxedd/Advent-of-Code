from dataclasses import dataclass
from enum import Enum
from math import floor
from typing import List


class PART(Enum):
    ONE = 0
    TWO = 1


@dataclass
class Monkey:
    items: List[int]
    operation: str = ""
    test_divis: int = 0
    if_true: int = 0
    if_false: int = 0
    interactions: int = 0

def str_to_int(x):
    return int(x)


def get_monkey_list(puzzle_input):
    monkey_list = []
    for line in puzzle_input:
        line = line.strip()
        if "Monkey" in line:
            monkey = Monkey(items=[])
        elif "Starting items:" in line:
            line = line.replace("Starting items: ", "")
            line = line.split(", ")
            monkey.items = list(map(str_to_int, line))
        elif "Operation" in line:
            line = line.replace("Operation: new = ", "")
            line = eval("lambda old:" + line)
            monkey.operation = line
        elif "Test" in line:
            line = line.replace("Test: divisible by ", "")
            monkey.test_divis = int(line)
        elif "If true" in line:
            line = line.replace("If true: throw to monkey ", "")
            monkey.if_true = int(line)
        elif "If false" in line:
            line = line.replace("If false: throw to monkey ", "")
            monkey.if_false = int(line)
            monkey_list.append(monkey)
    return monkey_list


def get_answer(part: PART):
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()
    monkey_list = get_monkey_list(puzzle_input)

    if part is PART.ONE:
        rounds = 20
    if part is PART.TWO:
        rounds = 10000

    for i in range(rounds):
        print(i)
        for monkey in monkey_list:
            for item in monkey.items:
                item_score = monkey.operation(item)
                if part is PART.ONE:
                    item_score = floor(item_score/3)
                if item_score % monkey.test_divis == 0:
                    monkey_list[monkey.if_true].items.append(item_score)
                else:
                    monkey_list[monkey.if_false].items.append(item_score)
                monkey.interactions += 1
            monkey.items = []

    sorted_list = sorted(monkey_list, key=lambda x: x.interactions)
    return sorted_list[-1].interactions * sorted_list[-2].interactions

print(get_answer(PART.ONE))
print(get_answer(PART.TWO))