def get_part_one_answer(puzzle_input):
    signal_nr = 0
    x = 1
    signal_strenghts = []

    signals_to_add = [20, 60, 100, 140, 180, 220]

    for line in puzzle_input:
        line = line.strip()
        if line == "noop":
            signal_nr += 1
            signal_strenghts.append(signal_nr * x)
        if "addx" in line:
            add_value = line.split(" ")[1]
            signal_nr += 1
            signal_strenghts.append(signal_nr * x)
            signal_nr += 1
            signal_strenghts.append(signal_nr * x)
            x += int(add_value)

    signal_sum = 0
    for index, signal_str in enumerate(signal_strenghts):
        if index + 1 in signals_to_add:
            signal_sum += signal_str
    return signal_sum


def get_part_two_answer(puzzle_input):
    screen = []
    puzzle_instructions = []
    for line in puzzle_input:
        puzzle_instructions.append(line.strip())

    x = 1
    row = 0
    add_x_in_next_iteration = False
    wait_iteration = False
    for signal_number in range(240):
        screen_position = signal_number % 40
        if screen_position == 0:
            screen.append([])
            row = len(screen) - 1

        if puzzle_instructions[0] == "noop":
            puzzle_instructions.pop(0)
        elif not add_x_in_next_iteration:
            if "addx" in puzzle_instructions[0]:
                add_x_in_next_iteration = True
                wait_iteration = True
                x_add_value = get_addx_value(puzzle_instructions)

        if screen_position_near_x(screen_position, x):
            screen[row].append("#")
        else:
            screen[row].append(".")

        if add_x_in_next_iteration and not wait_iteration:
            x += x_add_value
            add_x_in_next_iteration = False
            puzzle_instructions.pop(0)
        if wait_iteration:
            wait_iteration = False

    return get_part_two_answer_str(screen)


def screen_position_near_x(screen_position, x):
    return screen_position == x - 1 or screen_position == x or screen_position == x + 1


def get_addx_value(puzzle_instructions):
    return int(puzzle_instructions[0].split(" ")[1])


def get_part_two_answer_str(screen):
    answer_str = ""
    for line in screen:
        for char in line:
            answer_str += char
        answer_str += "\n"
    return answer_str


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    print("part one answer:", get_part_one_answer(puzzle_input))
    print("part two answer:")
    print(get_part_two_answer(puzzle_input))
