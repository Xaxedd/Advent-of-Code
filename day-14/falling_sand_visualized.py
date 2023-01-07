import time
from dataclasses import dataclass
from enum import Enum
from typing import List
import curses
from curses import wrapper

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
    return rock_structure_points_list



def get_cords(cords: str):
    splitted_cords = cords.split(",")
    return Cords(x=int(splitted_cords[0]),
                 y=int(splitted_cords[1]),
                 material=Material.AIR)


def delete_duplicates(rock_list: List[Cords]):
    stringified = set(map(to_str, rock_list))
    return list(map(to_cords, stringified))


def print_out_map(sorted_grid: List[Cords], sand_cords_rn: Cords):
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
            if sand_cords_rn.y == i and sand_cords_rn.x == j:
                row += "o"
                found = True
            if not found:
                row += "."
        all_rows.append(row)
    return all_rows


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


def add_falling_sand(stdscr, whole_sorted_grid):
    end = False
    while not end:
        index_to_change = 0
        sand_cord_rn = Cords(x=500, y=0, material=Material.SAND)
        while index_to_change == 0:
            # stdscr.addstr(amogus)
            long = ""
            rows = print_out_map(whole_sorted_grid, sand_cord_rn)
            stdscr.clear()
            for row in rows:
                stdscr.addstr(row+"\n")
            curses.delay_output(50)
            stdscr.refresh()
            # stdscr.addstr(long)
            # stdscr.refresh()
            time.sleep(0.01)
            material_under = get_coordinate_material(whole_sorted_grid, x=sand_cord_rn.x, y=sand_cord_rn.y + 1)
            if material_under is Material.AIR:
                sand_cord_rn.y = sand_cord_rn.y + 1
            if material_under is Material.ROCK or material_under is Material.SAND:
                material_under = get_coordinate_material(whole_sorted_grid, x=sand_cord_rn.x - 1, y=sand_cord_rn.y + 1)
                if material_under is Material.AIR:
                    sand_cord_rn.x = sand_cord_rn.x - 1
                    sand_cord_rn.y = sand_cord_rn.y + 1
                if material_under is Material.ROCK or material_under is Material.SAND:
                    material_under = get_coordinate_material(whole_sorted_grid, x=sand_cord_rn.x + 1, y=sand_cord_rn.y + 1)
                    if material_under is Material.AIR:
                        sand_cord_rn.x = sand_cord_rn.x + 1
                        sand_cord_rn.y = sand_cord_rn.y + 1
                    if material_under is Material.ROCK or material_under is Material.SAND:
                        whole_sorted_grid.append(Cords(x=sand_cord_rn.x, y=sand_cord_rn.y, material=Material.SAND))
                        break
            if sand_cord_rn.y > get_max_y(whole_sorted_grid):
                end = True
                break
    return whole_sorted_grid


def get_part_one_answer(stdscr, puzzle_input):
    whole_sorted_grid = get_rock_points_list(puzzle_input)
    whole_sorted_grid = add_falling_sand(stdscr, whole_sorted_grid)
    print_out_map(stdscr, whole_sorted_grid)
    sand_count = 0
    for cord in whole_sorted_grid:
        if cord.material is Material.SAND:
            sand_count += 1
    return sand_count


def main(stdscr):
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()
    whole_sorted_grid = get_rock_points_list(puzzle_input)
    stdscr.refresh()
    add_falling_sand(stdscr, whole_sorted_grid)
    stdscr.getch()


wrapper(main)

