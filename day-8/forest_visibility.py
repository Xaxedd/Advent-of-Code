from dataclasses import dataclass
from enum import Enum


@dataclass
class Cords:
    x: int
    y: int
    height: int
    already_added: bool


class Sides(Enum):
    TOP = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 3


def get_part_one_answer():
    coordinates_list = get_coordinates_list()
    trees_sum = find_all_visible_trees_sum(coordinates_list)

    return trees_sum


def get_coordinates_list():
    coordinates_list = []
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    for index_y, line in enumerate(puzzle_input):
        line = line.strip()
        for index_x, char in enumerate(line):
            xxx = Cords(x=index_x,
                        y=index_y,
                        height=int(char),
                        already_added=False)

            if is_tree_on_border(xxx):
                xxx.already_added = True

            coordinates_list.append(xxx)
    return coordinates_list


def find_all_visible_trees_sum(coordinates_list):
    find_visible_trees_from_sides(coordinates_list, look_from=Sides.LEFT)
    find_visible_trees_from_sides(coordinates_list, look_from=Sides.RIGHT)
    find_visible_trees_from_sides(coordinates_list, look_from=Sides.TOP)
    find_visible_trees_from_sides(coordinates_list, look_from=Sides.BOTTOM)

    suma = 0
    for cord in coordinates_list:
        if cord.already_added:
            suma += 1
    return suma


def find_visible_trees_from_sides(coordinates_list, look_from: Sides):
    sorted_list = sort_coordinates_list_for_side_part_one(coordinates_list, look_from)
    cord_right_now = 0
    max_height = 0
    for cord in sorted_list:
        if look_from is Sides.RIGHT or look_from is Sides.LEFT:
            if cord.y is not cord_right_now:
                cord_right_now = cord.y
                max_height = 0
        if look_from is Sides.TOP or look_from is Sides.BOTTOM:
            if cord.x is not cord_right_now:
                cord_right_now = cord.x
                max_height = 0

        if cord.height > max_height:
            cord.already_added = True
            max_height = cord.height
    return sorted_list


def sort_coordinates_list_for_side_part_one(coordinates_list, side: Sides):
    if side is Sides.TOP:
        return sorted(coordinates_list, key=lambda x: (x.x, x.y), reverse=True)
    if side is Sides.LEFT:
        return sorted(coordinates_list, key=lambda x: x.y)
    if side is Sides.RIGHT:
        return sorted(coordinates_list, key=lambda x: (x.y, x.x), reverse=True)
    if side is Sides.BOTTOM:
        return sorted(coordinates_list, key=lambda x: x.x)


def is_tree_on_border(cords: Cords):
    return cords.x == 0 or cords.x == 98 or cords.y == 0 or cords.y == 98


def get_part_two_answer():
    coordinates_list = get_coordinates_list()
    score_list = []
    for tree in coordinates_list:
        score = check_all_sides_from_point(coordinates_list, tree)
        score_list.append(score)
    score_list.sort()
    return score_list[-1]


def check_all_sides_from_point(coordinates_list, tree):
    return find_visible_trees_from_point(coordinates_list, tree, Sides.TOP) * \
           find_visible_trees_from_point(coordinates_list, tree, Sides.LEFT) * \
           find_visible_trees_from_point(coordinates_list, tree, Sides.RIGHT) * \
           find_visible_trees_from_point(coordinates_list, tree, Sides.BOTTOM)


def find_visible_trees_from_point(coordinates_list, tree: Cords, look_to: Sides):
    sorted_list = sort_coordinates_list_for_side_part_two(coordinates_list, look_to)
    if is_tree_on_border(tree):
        return 0

    amount_of_trees_seen = 0
    for cord in sorted_list:
        if cord_in_tree_line(cord, tree, look_to):
            if cord.height >= tree.height or is_tree_on_border(cord):
                amount_of_trees_seen += 1
                return amount_of_trees_seen
            if cord.height < tree.height:
                amount_of_trees_seen += 1


def sort_coordinates_list_for_side_part_two(coordinates_list, side: Sides):
    if side is Sides.TOP:
        return sorted(coordinates_list, key=lambda x: (x.x, x.y), reverse=True)
    if side is Sides.LEFT:
        return sorted(coordinates_list, key=lambda x: (x.y, x.x), reverse=True)
    if side is Sides.RIGHT:
        return sorted(coordinates_list, key=lambda x: x.y)
    if side is Sides.BOTTOM:
        return sorted(coordinates_list, key=lambda x: (x.x, x.y))


def cord_in_tree_line(cord, tree, look_to) -> bool:
    if look_to is Sides.RIGHT:
        return cord.y == tree.y and cord.x > tree.x
    if look_to is Sides.LEFT:
        return cord.y == tree.y and cord.x < tree.x
    if look_to is Sides.TOP:
        return cord.x == tree.x and cord.y < tree.y
    if look_to is Sides.BOTTOM:
        return cord.x == tree.x and cord.y > tree.y


if __name__ == "__main__":
    print("part one answer:", get_part_one_answer())
    print("part two answer:", get_part_two_answer())
