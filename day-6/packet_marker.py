def get_part_one_answer(signal):
    return get_index_of_first_distinct_chars_in_str(signal, amount_of_distinct_chars=4)


def get_part_two_answer(signal):
    return get_index_of_first_distinct_chars_in_str(signal, amount_of_distinct_chars=14)


def get_index_of_first_distinct_chars_in_str(signal, amount_of_distinct_chars):
    last_chars = []
    char_index = 0
    for char in signal:
        last_chars.append(char)
        char_index += 1
        if len(last_chars) == amount_of_distinct_chars:
            check_duplicates = set(last_chars)
            if len(check_duplicates) == amount_of_distinct_chars:
                return char_index
            last_chars.pop(0)


def main():
    signal = open("puzzle_input.txt", "r", encoding="utf8").readlines()[0]
    print("part one answer:", get_part_one_answer(signal))
    print("part two answer:", get_part_two_answer(signal))


if __name__ == '__main__':
    main()
