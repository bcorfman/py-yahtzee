from collections import Counter


def _first_of(num, lst):
    return lst[:num] if len(lst) >= num else [0] * num


def _highest_matches_of(num_matching, dice):
    score_matching = [k * num_matching for k, v in Counter(dice).items() if v == num_matching]
    return list(reversed(sorted(score_matching)))


def _sequence_starting_with(num, dice):
    sorted_dice = list(sorted(dice))
    straight = list(range(num, num+5))
    return sum(sorted_dice) if sorted_dice == straight else 0


def same_number(num, dice):
    return sum([die for die in dice if die == num]) if num in dice else 0


def pair(dice):
    return sum(_first_of(1, _highest_matches_of(2, dice)))


def two_pair(dice):
    return sum(_first_of(2, _highest_matches_of(2, dice)))


def three_of_a_kind(dice):
    return sum(_first_of(1, _highest_matches_of(3, dice)))


def four_of_a_kind(dice):
    return sum(_first_of(1, _highest_matches_of(4, dice)))


def small_straight(dice):
    return _sequence_starting_with(1, dice)


def large_straight(dice):
    return _sequence_starting_with(2, dice)


def full_house(dice):
    return sum(_first_of(1, _highest_matches_of(3, dice))) + sum(_first_of(1, _highest_matches_of(2, dice)))


def yahtzee(dice):
    return 50 if sum(_first_of(1, _highest_matches_of(5, dice))) else 0


def chance(dice):
    return sum(dice)
