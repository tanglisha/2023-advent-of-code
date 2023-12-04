from  .code import Game

def test_process_line():
    game1 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    assert game1.rounds[0].red == 6
    assert game1.rounds[0].blue ==  1
    assert game1.rounds[0].green == 3
    assert game1.rounds[1].red == 1
    assert game1.rounds[1].blue == 2
    assert game1.rounds[1].green ==  2

    game2 = Game("Game 2: 2 green; 15 red, 5 blue; 2 green, 4 blue, 5 red; 3 green, 6 blue, 6 red; 6 blue, 1 green")
    assert game2.rounds[0].red == 0
    assert game2.rounds[0].blue ==  0
    assert game2.rounds[0].green == 2
    assert game2.rounds[1].red == 15
    assert game2.rounds[1].blue == 5
    assert game2.rounds[1].green == 0

def test_possible():
    game1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    game2 = Game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    game3 = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    game4 = Game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    game5 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    game6 =  Game("Game 95: 9 blue, 11 green; 14 green, 10 blue, 11 red; 13 blue, 10 green, 1 red; 6 red, 4 green, 1 blue; 9 blue, 13 green")

    assert game1.check_possible(red=12, green=13, blue=14)
    assert game2.check_possible(red=12, green=13, blue=14)
    assert game3.check_possible(red=12, green=13, blue=14) is False
    assert game4.check_possible(red=12, green=13, blue=14) is False
    assert game5.check_possible(red=12, green=13, blue=14)
    assert game6.check_possible(red=12, green=13, blue=14) is False


def test_min_cubes():
    game1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game1.find_mins() == (4, 2, 6)

def test_power_mins():
    game1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game1.power_mins() == 48
