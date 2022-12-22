import re


def get_part_one_answer():
    directories = get_directories()

    suma = 0
    for value in directories.values():
        if value <= 100000:
            suma += value
    return suma


def get_part_two_answer():
    directories = get_directories()

    storage_sum = 70000000
    space_available = storage_sum - directories["/"]
    lowest_good = 99999999999
    best_directory_size = 0
    if storage_sum - directories["/"] < 30000000:
        for directory in directories.values():
            space_available_after_delete = space_available + directory
            if 30000000 <= space_available_after_delete < lowest_good:
                lowest_good = space_available_after_delete
                best_directory_size = directory

    return best_directory_size


def take_out_int_from_str(string: str):  # returns first int in string
    return int(re.search(r'\d+', string).group())


def get_directories():
    directories = {"/": 0}
    list_of_adds = []

    for line in puzzle_input:
        line = line.strip()
        try:
            file_size = take_out_int_from_str(line)
        except:
            file_size = 0
        if line == "$ cd /":
            list_of_adds = ["/"]

        elif file_size != 0:
            for directory in list_of_adds:
                directories[directory] += file_size

        elif line == "$ cd ..":
            list_of_adds.pop()

        elif "cd" in line:
            splitted = line.split(" ")
            directory_name = list_of_adds[-1] + "/" + splitted[-1]
            list_of_adds.append(directory_name)
            directories[directory_name] = 0
    return directories


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    print("part one answer:", get_part_one_answer())
    print("part two answer:", get_part_two_answer())
