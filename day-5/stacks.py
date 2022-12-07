import re
from dataclasses import dataclass
from typing import List


@dataclass
class Crane:
    amount_of_boxes: int
    taken_from_stack: int
    given_to_stack: int


def get_part_one_answer(puzzle_input):
    stacks = [["W", "R", "F"],
              ["T", "H", "M", "C", "D", "V", "W", "P"],
              ["P", "M", "Z", "N", "L"],
              ["J", "C", "H", "R"],
              ["C", "P", "G", "H", "Q", "T", "B"],
              ["G", "C", "W", "L", "F", "Z"],
              ["W", "V", "L", "Q", "Z", "J", "G", "C"],
              ["P", "N", "R", "F", "W", "T", "V", "C"],
              ["J", "W", "H", "G", "R", "S", "V"]]

    for line in puzzle_input:
        line = line.strip()
        if "move" in line:
            stack_info = get_stacks_info(line)
            for i in range(stack_info.amount_of_boxes):
                stacks[stack_info.given_to_stack].append(stacks[stack_info.taken_from_stack][-1])
                stacks[stack_info.taken_from_stack].pop()
    return get_final_string(stacks)


def get_part_two_answer(puzzle_input):
    stacks = [["W", "R", "F"],
              ["T", "H", "M", "C", "D", "V", "W", "P"],
              ["P", "M", "Z", "N", "L"],
              ["J", "C", "H", "R"],
              ["C", "P", "G", "H", "Q", "T", "B"],
              ["G", "C", "W", "L", "F", "Z"],
              ["W", "V", "L", "Q", "Z", "J", "G", "C"],
              ["P", "N", "R", "F", "W", "T", "V", "C"],
              ["J", "W", "H", "G", "R", "S", "V"]]

    for line in puzzle_input:
        line = line.strip()
        if "move" in line:
            stack_info = get_stacks_info(line)
            dummy_stack = []
            for i in range(stack_info.amount_of_boxes):
                dummy_stack.append(stacks[stack_info.taken_from_stack][-1])
                stacks[stack_info.taken_from_stack].pop()
            dummy_stack.reverse()
            for i in dummy_stack:
                stacks[stack_info.given_to_stack].append(i)
    return get_final_string(stacks)


def get_stacks_info(line) -> Crane:
    list_of_nums = get_all_ints_from_str(line)
    stack = Crane(amount_of_boxes=list_of_nums[0],
                  taken_from_stack=list_of_nums[1] - 1,
                  given_to_stack=list_of_nums[2] - 1)
    return stack


def get_all_ints_from_str(string: str) -> List[int]:
    return list(map(int, re.findall('\d+', string)))


def get_final_string(stacks):
    final_str = ""
    for stack in stacks:
        final_str += stack[-1]
    return final_str


def main():
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    print("part one answer:", get_part_one_answer(puzzle_input))
    print("part two answer:", get_part_two_answer(puzzle_input))


if __name__ == '__main__':
    main()
