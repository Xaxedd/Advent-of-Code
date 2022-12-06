from typing import List


def split_string_in_two(string: str) -> [str, str]:
    return string[:len(string) // 2], string[len(string) // 2:]


def get_char_score(char):
    int_of_char = ord(char)
    if int_of_char <= 90:
        return int_of_char - 38
    if int_of_char >= 97:
        return int_of_char - 96


def get_score_of_common_elements(common_elements: List):
    common_elements_sum = 0
    for char in common_elements:
        int_of_char = get_char_score(char)
        common_elements_sum += int_of_char
    return common_elements_sum


def get_part_one_answer(rucksacks_list: List):
    common_elements = []
    for rucksack in rucksacks_list:
        rucksack = rucksack.strip()
        backpack_first_half, backpack_second_half = split_string_in_two(rucksack)
        for char in backpack_first_half:
            if char in backpack_second_half:
                common_elements.append(char)
                break

    common_elements_sum = get_score_of_common_elements(common_elements)
    return common_elements_sum


def get_part_two_answer(rucksacks_list: List):
    common_elements = []
    trio_of_rucksacks = []
    for rucksack in rucksacks_list:
        rucksack = rucksack.strip()
        trio_of_rucksacks.append(rucksack)

        if len(trio_of_rucksacks) == 3:
            intersection = list(set(trio_of_rucksacks[0]) & set(trio_of_rucksacks[1]) & set(trio_of_rucksacks[2]))
            common_elements.append(intersection[0])
            trio_of_rucksacks = []
    common_elements_sum = get_score_of_common_elements(common_elements)
    return common_elements_sum

def main():
    rucksacks_list = open("rucksack_contents.txt", "r", encoding="utf8").readlines()
    print("part one answer:", get_part_one_answer(rucksacks_list))
    print("part two answer:", get_part_two_answer(rucksacks_list))

if __name__ == '__main__':
    main()
