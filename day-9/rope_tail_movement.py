from dataclasses import dataclass


@dataclass
class Cords:
    x: int
    y: int


def move_head(head, direction):
    if direction == "R":
        head.x += 1
    if direction == "L":
        head.x -= 1
    if direction == "U":
        head.y += 1
    if direction == "D":
        head.y -= 1
    return head


def move_tail(head, tail):
    if tail.x - head.x == 2 and tail.y == head.y:
        tail.x -= 1
    if tail.x - head.x == -2 and tail.y == head.y:
        tail.x += 1
    if tail.y - head.y == 2 and tail.x == head.x:
        tail.y -= 1
    if tail.y - head.y == -2 and tail.x == head.x:
        tail.y += 1
    if (tail.x - head.x == 2 and tail.y - head.y == -1) or (tail.y - head.y == -2 and tail.x - head.x == 1):
        tail.x -= 1
        tail.y += 1
    if (tail.x - head.x == 2 and tail.y - head.y == 1) or (tail.y - head.y == 2 and tail.x - head.x == 1):
        tail.x -= 1
        tail.y -= 1
    if (tail.x - head.x == -2 and tail.y - head.y == -1) or (tail.y - head.y == -2 and tail.x - head.x == -1):
        tail.x += 1
        tail.y += 1
    if (tail.x - head.x == -2 and tail.y - head.y == 1) or (tail.y - head.y == 2 and tail.x - head.x == -1):
        tail.y -= 1
        tail.x += 1
    if tail.x - head.x == -2 and tail.y - head.y == -2:
        tail.x += 1
        tail.y += 1
    if tail.x - head.x == 2 and tail.y - head.y == -2:
        tail.x -= 1
        tail.y += 1
    if tail.x - head.x == -2 and tail.y - head.y == 2:
        tail.x += 1
        tail.y -= 1
    if tail.x - head.x == 2 and tail.y - head.y == 2:
        tail.x -= 1
        tail.y -= 1

    return tail


def get_part_one_answer(puzzle_input):
    head = Cords(x=0, y=0)
    tail = Cords(x=0, y=0)
    tail_cords_list = set()

    for line in puzzle_input:
        line = line.strip()
        direction, steps = line.split(" ")
        steps = int(steps)
        for i in range(steps):
            head = move_head(head, direction)
            tail = move_tail(head, tail)
            tail_cords_list.add("x" + str(tail.x) + "y" + str(tail.y))

    return len(tail_cords_list)


def get_part_two_answer(puzzle_input):
    rope_knots = []
    tail_cords_list = set()
    for i in range(10):
        rope_knots.append(Cords(x=0, y=0))

    for line in puzzle_input:
        line = line.strip()
        direction, steps = line.split(" ")
        steps = int(steps)
        for i in range(steps):
            rope_knots[0] = move_head(rope_knots[0], direction)
            for j in range(1, 10):
                rope_knots[j] = move_tail(rope_knots[j - 1], rope_knots[j])
            tail_cords_list.add("x" + str(rope_knots[-1].x) + "y" + str(rope_knots[-1].y))
    return len(tail_cords_list)


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    print("part one answer:", get_part_one_answer(puzzle_input))
    print("part two answer:", get_part_two_answer(puzzle_input))
