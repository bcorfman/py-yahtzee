from collections import Counter


def _top(num, lst):
    return lst[:num] if len(lst) >= num else [0] * num


def _highest_matching_groups(num_matching, dice):
    score_matching = [k * num_matching for k, v in Counter(dice).items() if v == num_matching]
    return list(reversed(sorted(score_matching)))


def _straight(starting_number, dice):
    sorted_dice = list(sorted(dice))
    straight = list(range(starting_number, starting_number+5))
    return sum(sorted_dice) if sorted_dice == straight else 0


def same_number(num, dice):
    return sum([die for die in dice if die == num]) if num in dice else 0


def pair(dice):
    return sum(_top(1, _highest_matching_groups(2, dice)))


def two_pair(dice):
    return sum(_top(2, _highest_matching_groups(2, dice)))


def three_of_a_kind(dice):
    return sum(_top(1, _highest_matching_groups(3, dice)))


def four_of_a_kind(dice):
    return sum(_top(1, _highest_matching_groups(4, dice)))


def small_straight(dice):
    return _straight(1, dice)


def large_straight(dice):
    return _straight(2, dice)


def full_house(dice):
    return sum(_top(1, _highest_matching_groups(3, dice))) + sum(_top(1, _highest_matching_groups(2, dice)))


def yahtzee(dice):
    return 50 if sum(_top(1, _highest_matching_groups(5, dice))) else 0


def chance(dice):
    return sum(dice)
