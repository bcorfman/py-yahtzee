import yahtzee


def test_same_number():
    assert 8 == yahtzee.same_number(4, [1, 1, 2, 4, 4])


def test_first_of():
    assert [8] == yahtzee._first_of(1, [8, 6])
    assert [8, 6] == yahtzee._first_of(2, [8, 6, 4])
    assert [0, 0] == yahtzee._first_of(2, [8])


def test_highest_matches_of():
    assert list(yahtzee._highest_matches_of(2, [5, 5, 4, 4, 2])) == [10, 8]
    assert list(yahtzee._highest_matches_of(2, [6, 6, 4, 4, 5])) == [12, 8]
    assert list(yahtzee._highest_matches_of(2, [5, 4, 3, 2, 1])) == []


def test_pair():
    assert 8 == yahtzee.pair([3, 3, 3, 4, 4])


def test_two_pair():
    assert 8 == yahtzee.two_pair([1, 1, 2, 3, 3])
    assert 0 == yahtzee.two_pair([1, 2, 3, 4, 5])


def test_three_of_a_kind():
    assert 9 == yahtzee.three_of_a_kind([3, 3, 3, 4, 5])
    assert 0 == yahtzee.three_of_a_kind([3, 3, 3, 3, 5])
    assert 0 == yahtzee.three_of_a_kind([3, 3, 2, 4, 5])


def test_four_of_a_kind():
    assert 8 == yahtzee.four_of_a_kind([2, 2, 2, 2, 5])
    assert 0 == yahtzee.four_of_a_kind([2, 2, 2, 2, 2])
    assert 0 == yahtzee.four_of_a_kind([3, 3, 3, 4, 5])


def test_small_straight():
    assert 15 == yahtzee.small_straight([1, 2, 3, 4, 5])
    assert 0 == yahtzee.small_straight([2, 3, 4, 5, 6])


def test_large_straight():
    assert 0 == yahtzee.large_straight([1, 2, 3, 4, 5])
    assert 20 == yahtzee.large_straight([2, 3, 4, 5, 6])


def test_full_house():
    assert 8 == yahtzee.full_house([1, 1, 2, 2, 2])
    assert 0 == yahtzee.full_house([4, 4, 4, 4, 4])


def test_yahtzee():
    assert 50 == yahtzee.yahtzee([1, 1, 1, 1, 1])
    assert 0 == yahtzee.yahtzee([1, 2, 1, 1, 1])


def test_chance():
    assert 17 == yahtzee.chance([1, 3, 3, 4, 6])
    assert 5 == yahtzee.chance([1, 1, 1, 1, 1])
