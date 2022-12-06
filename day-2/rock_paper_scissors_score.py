from enum import Enum


class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def points_for_my_hand(my_hand):
    if my_hand is Hand.ROCK:
        return 1
    elif my_hand is Hand.PAPER:
        return 2
    elif my_hand is Hand.SCISSORS:
        return 3


def get_game_outcome_part_one(my_hand: Hand, opponents_hand: Hand) -> int:
    if my_hand is Hand.ROCK:
        if opponents_hand is Hand.ROCK:
            return 3
        elif opponents_hand is Hand.PAPER:
            return 0
        elif opponents_hand is Hand.SCISSORS:
            return 6
    elif my_hand is Hand.PAPER:
        if opponents_hand is Hand.ROCK:
            return 6
        elif opponents_hand is Hand.PAPER:
            return 3
        elif opponents_hand is Hand.SCISSORS:
            return 0
    elif my_hand is Hand.SCISSORS:
        if opponents_hand is Hand.ROCK:
            return 0
        elif opponents_hand is Hand.PAPER:
            return 6
        elif opponents_hand is Hand.SCISSORS:
            return 3


def get_part_one_answer(matches_list):
    total_score = 0
    for line in matches_list:
        hands = line.strip().split(" ")
        opponent_hand = change_letter_to_xxx(hands[0])
        my_hand = change_letter_to_xxx(hands[1])

        total_score += points_for_my_hand(my_hand)
        total_score += get_game_outcome_part_one(my_hand, opponent_hand)
    return total_score


def get_game_outcome_part_two(my_hand: Hand, opponents_hand: Hand) -> int:
    if my_hand is Hand.ROCK:
        if opponents_hand is Hand.ROCK:
            return 3
        elif opponents_hand is Hand.PAPER:
            return 1
        elif opponents_hand is Hand.SCISSORS:
            return 2
    elif my_hand is Hand.PAPER:
        if opponents_hand is Hand.ROCK:
            return 4
        elif opponents_hand is Hand.PAPER:
            return 5
        elif opponents_hand is Hand.SCISSORS:
            return 6
    elif my_hand is Hand.SCISSORS:
        if opponents_hand is Hand.ROCK:
            return 8
        elif opponents_hand is Hand.PAPER:
            return 9
        elif opponents_hand is Hand.SCISSORS:
            return 7


def get_part_two_answer(matches_list):
    total_score = 0
    for line in matches_list:
        hands = line.strip().split(" ")
        opponent_hand = change_letter_to_xxx(hands[0])
        my_hand = change_letter_to_xxx(hands[1])

        total_score += get_game_outcome_part_two(my_hand, opponent_hand)
    return total_score


def change_letter_to_xxx(hand) -> Hand:
    if hand == "A":
        return Hand.ROCK
    if hand == "B":
        return Hand.PAPER
    if hand == "C":
        return Hand.SCISSORS
    if hand == "X":
        return Hand.ROCK
    if hand == "Y":
        return Hand.PAPER
    if hand == "Z":
        return Hand.SCISSORS


matches_list = open("rps_matches.txt", "r", encoding="utf8").readlines()
print("part one answer:", get_part_one_answer(matches_list))
print("part two answer:", get_part_two_answer(matches_list))