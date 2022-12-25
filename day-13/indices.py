from enum import Enum


class ListEnum(Enum):
    LEFT = 0
    RIGHT = 1


def get_part_one_answer():
    pairs = get_puzzle_pairs()
    right_order_pairs = 0
    index_sum = 0
    for index, pair in enumerate(pairs):
        left = pair[0]
        right = pair[1]
        order_found, order_is_good = recurrent_solution(left, right)

        if order_is_good:
            right_order_pairs += 1
            index_sum += index + 1
    return index_sum


def get_part_two_answer():
    signals = get_signals_list()
    signals.append([[2]])
    signals.append([[6]])

    signals = bubble_sort_signals(signals)

    first_packet = 0
    second_packet = 0
    for index, signal in enumerate(signals):
        signal = str(signal)
        if signal == "[[2]]":
            first_packet = index + 1
        if signal == "[[6]]":
            second_packet = index + 1
    return first_packet * second_packet


def get_puzzle_pairs():
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    xxx = 0
    left = ""
    right = ""
    pairs = []
    for line in puzzle_input:
        line = line.strip()
        if xxx == 0:
            left = eval(line)
            xxx += 1
        elif xxx == 1:
            right = eval(line)
            xxx += 1
        elif xxx == 2:
            pairs.append([left, right])
            xxx = 0
    return pairs


def get_signals_list():
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()
    signal_list = []

    for line in puzzle_input:
        line = line.strip()

        if line != "":
            signal_list.append(eval(line))
    return signal_list


def bubble_sort_signals(signals):
    all_good = False
    while not all_good:
        good = 0
        i = 1
        while i < len(signals):
            order_found, order_is_good = recurrent_solution(signals[i - 1], signals[i])
            if order_is_good:
                good += 1
            else:
                switch = signals[i - 1]
                signals[i - 1] = signals[i]
                signals[i] = switch
            i += 1
        if good + 1 == len(signals):
            all_good = True
    return signals


def recurrent_solution(left, right):
    order_found = False
    order_is_good = False

    smaller_list, smaller_list_enum = find_smaller_list(left, right)
    for i in range(len(smaller_list)):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                order_found = True
                order_is_good = True
            if left[i] > right[i]:
                order_found = True
                order_is_good = False
            if left[i] == right[i]:
                pass

        elif type(left[i]) is None and type(right[i]) is not None:
            order_found = True
            order_is_good = True
        elif type(left[i]) is not None and type(right[i]) is None:
            order_found = True
            order_is_good = False
        elif type(left[i]) is None and type(right[i]) is None:
            pass

        elif isinstance(left[i], list) and isinstance(right[i], list):
            order_found, order_is_good = recurrent_solution(left[i], right[i])
        elif isinstance(left[i], int) and isinstance(right[i], list):
            order_found, order_is_good = recurrent_solution(eval(f"[{left[i]}]"), right[i])
        elif isinstance(left[i], list) and isinstance(right[i], int):
            order_found, order_is_good = recurrent_solution(left[i], eval(f"[{right[i]}]"))

        if order_found:
            return order_found, order_is_good
    if len(left) != len(right):
        if smaller_list_enum is ListEnum.LEFT:
            order_found = True
            order_is_good = True
        else:
            order_found = True
            order_is_good = False
    return order_found, order_is_good


def find_smaller_list(left, right):
    if len(left) < len(right):
        smaller_list = left
        smaller_list_enum = ListEnum.LEFT
    else:
        smaller_list = right
        smaller_list_enum = ListEnum.RIGHT
    return smaller_list, smaller_list_enum


if __name__ == "__main__":
    print("part one answer:", get_part_one_answer())
    print("part two answer:", get_part_two_answer())

