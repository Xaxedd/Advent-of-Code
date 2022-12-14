from dataclasses import dataclass
from enum import Enum
from typing import List


class Material(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2


@dataclass
class Cords:
    x: int
    y: int
    material: Material


def to_str(x):
    return str(x)


def to_cords(x):
    x = x.replace("<", "")
    x = x.replace(": 1>", "")
    return eval(x)


def get_rock_points_list(puzzle_input):
    rock_structure_points_list = []
    for line in puzzle_input:
        line = line.strip()
        starting_points = line.split(" -> ")

        if len(starting_points) >= 2:
            index = 1
            while index < len(starting_points):
                start_cords = get_cords(starting_points[index - 1])
                ending_cords = get_cords(starting_points[index])
                if start_cords.x == ending_cords.x:
                    if start_cords.y >= ending_cords.y:
                        for i in range(ending_cords.y, start_cords.y + 1):
                            rock_structure_points_list.append(Cords(x=start_cords.x, y=i, material=Material.ROCK))
                    else:
                        for i in range(start_cords.y, ending_cords.y + 1):
                            rock_structure_points_list.append(Cords(x=start_cords.x, y=i, material=Material.ROCK))

                if start_cords.y == ending_cords.y:
                    if start_cords.x >= ending_cords.x:
                        for i in range(ending_cords.x, start_cords.x + 1):
                            rock_structure_points_list.append(Cords(x=i, y=start_cords.y, material=Material.ROCK))
                    else:
                        for i in range(start_cords.x, ending_cords.x + 1):
                            rock_structure_points_list.append(Cords(x=i, y=start_cords.y, material=Material.ROCK))
                index += 1
    rock_structure_points_list = delete_duplicates(rock_structure_points_list)
    sorted_grid = sorted(rock_structure_points_list, key=lambda x: (x.y, x.x))
    return sorted_grid



def get_cords(cords: str):
    splitted_cords = cords.split(",")
    return Cords(x=int(splitted_cords[0]),
                 y=int(splitted_cords[1]),
                 material=Material.AIR)


def delete_duplicates(rock_list: List[Cords]):
    stringified = set(map(to_str, rock_list))
    return list(map(to_cords, stringified))


def print_out_map(sorted_grid: List[Cords]):
    all_rows = []
    min_x = get_min_x(sorted_grid)
    max_x = get_max_x(sorted_grid)
    max_y = get_max_y(sorted_grid)
    for i in range(max_y + 1):
        row = ""
        for j in range(min_x, max_x + 1):
            found = False
            for structure in sorted_grid:
                if structure.y == i and structure.x == j:
                    if structure.material is Material.ROCK:
                        row += "#"
                    elif structure.material is Material.SAND:
                        row += "o"
                    found = True
            if not found:
                row += "."
        all_rows.append(row)
    for row in all_rows:
        print(row)


def get_coordinate_material(grid: List[Cords], x: int, y: int):
    for cord in grid:
        if cord.x == x and cord.y == y:
            return cord.material
    return Material.AIR


def get_max_y(rock_structure_points_list):
    sort2 = sorted(rock_structure_points_list, key=lambda x: (x.y, x.x))
    return sort2[-1].y


def get_min_x(rock_structure_points_list):
    sort = sorted(rock_structure_points_list, key=lambda x: (x.x, x.y))
    return sort[0].x


def get_max_x(rock_structure_points_list):
    sort = sorted(rock_structure_points_list, key=lambda x: (x.x, x.y))
    return sort[-1].x


def delete_unreachable_cords(usable_coordinates: List[Cords], for_visualization: List[Cords]):
    good_cords = []
    for usable_cord in usable_coordinates:
        needed_cord = True
        if get_coordinate_material(for_visualization, x=usable_cord.x, y=usable_cord.y-1) is not Material.AIR:
            if get_coordinate_material(for_visualization, x=usable_cord.x-1, y=usable_cord.y) is not Material.AIR and \
               get_coordinate_material(for_visualization, x=usable_cord.x+1, y=usable_cord.y) is not Material.AIR:
                if get_coordinate_material(for_visualization, x=usable_cord.x-1, y=usable_cord.y-1) is not Material.AIR and \
                   get_coordinate_material(for_visualization, x=usable_cord.x+1, y=usable_cord.y-1) is not Material.AIR:
                    if get_coordinate_material(for_visualization, x=usable_cord.x-2, y=usable_cord.y) is not Material.AIR and \
                       get_coordinate_material(for_visualization, x=usable_cord.x+2, y=usable_cord.y) is not Material.AIR:
                        needed_cord = False
        if needed_cord:
            good_cords.append(usable_cord)
    return good_cords

def add_falling_sand(whole_sorted_grid):
    coordinates_for_sand = whole_sorted_grid
    coordinates_for_sand = delete_unreachable_cords(coordinates_for_sand, whole_sorted_grid)
    end = False
    sand_nr = 0
    while not end:
        sand_nr += 1
        if sand_nr % 50 == 0:
            coordinates_for_sand = delete_unreachable_cords(coordinates_for_sand, whole_sorted_grid)
        sand_cord_rn = Cords(x=500, y=0, material=Material.SAND)
        while True:
            material_under = get_coordinate_material(coordinates_for_sand, x=sand_cord_rn.x, y=sand_cord_rn.y + 1)
            if material_under is Material.AIR:
                sand_cord_rn.y = sand_cord_rn.y + 1
            if material_under is Material.ROCK or material_under is Material.SAND:
                material_under = get_coordinate_material(coordinates_for_sand, x=sand_cord_rn.x - 1, y=sand_cord_rn.y + 1)
                if material_under is Material.AIR:
                    sand_cord_rn.x = sand_cord_rn.x - 1
                    sand_cord_rn.y = sand_cord_rn.y + 1
                if material_under is Material.ROCK or material_under is Material.SAND:
                    material_under = get_coordinate_material(coordinates_for_sand, x=sand_cord_rn.x + 1, y=sand_cord_rn.y + 1)
                    if material_under is Material.AIR:
                        sand_cord_rn.x = sand_cord_rn.x + 1
                        sand_cord_rn.y = sand_cord_rn.y + 1
                    if material_under is Material.ROCK or material_under is Material.SAND:
                        whole_sorted_grid.append(Cords(x=sand_cord_rn.x, y=sand_cord_rn.y, material=Material.SAND))
                        coordinates_for_sand.append(Cords(x=sand_cord_rn.x, y=sand_cord_rn.y, material=Material.SAND))
                        break
            if sand_cord_rn.y > get_max_y(whole_sorted_grid):
                end = True
                break
    sand_sum = 0
    for cord in coordinates_for_sand:
        if cord.material is not Material.AIR:
            sand_sum += 1
    print("without dupes:", sand_sum)
    print_out_map(coordinates_for_sand)
    return whole_sorted_grid


def get_part_one_answer(puzzle_input):
    whole_sorted_grid = get_rock_points_list(puzzle_input)
    # print_out_map(whole_sorted_grid)
    whole_sorted_grid = add_falling_sand(whole_sorted_grid)
    print_out_map(whole_sorted_grid)
    sand_sum = 0
    for cord in whole_sorted_grid:
        if cord.material is not Material.AIR:
            sand_sum += 1
    print("noraml", sand_sum)
    sand_count = 0
    for cord in whole_sorted_grid:
        if cord.material is Material.SAND:
            sand_count += 1
    return sand_count


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    print("part one answer:", get_part_one_answer(puzzle_input))