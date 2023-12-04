#!/usr/bin/env python

class Round:
    red: int = 0
    blue: int = 0
    green: int = 0

    def __init__(self, input_rounds: str):
        for item in input_rounds.split(","):
            item = item.strip()
            num_cubes, color = item.split(" ")
            num_cubes = int(num_cubes)

            match color:
                case "red":
                    self.red = num_cubes
                case "blue":
                    self.blue = num_cubes
                case "green":
                    self.green = num_cubes


class Game:
    id: int
    rounds: list[Round]
    original_line: str

    def __init__(self, input_line: str):
        self.original_line = input_line
        self.id = int(input_line.split(":")[0][5:])
        round_string = input_line.split(":")[1]
        self.rounds = []

        for round in round_string.split(";"):
            self.rounds.append(Round(round))

    def check_possible(self, red: int, blue: int, green: int):
        for round in self.rounds:
            if red < round.red or \
            blue < round.blue or \
            green < round.green:
                return False
        print(self.original_line)
        return True
    
    def find_mins(self) -> tuple[int]:
        """
        Returns a tuple of the minimum possible values
        """
        min_red = 0
        min_blue = 0
        min_green = 0

        for round in self.rounds:
            if round.blue > min_blue:
                min_blue = round.blue
            if round.red > min_red:
                min_red = round.red
            if round.green > min_green:
                min_green = round.green

        return (min_red, min_green, min_blue)
    
    def power_mins(self) -> int:
        """
        Find the power value of the minimum possible
        """
        total = 1

        mins = self.find_mins()

        for item in mins:
            total *= item

        return total
    
if "__main__" == __name__:
    with open("day2/input.txt", "r") as input:
        lines = input.readlines()
    
    total_gameids = 0
    total_pow = 0

    for line in lines:
        game = Game(line)
        if game.check_possible(red=12, blue=14, green=13):
            # print(f"adding game {game.id} to the total {total_gameids}")
            total_gameids += game.id
        total_pow += game.power_mins()

    print(f"The sum of the games that fit the red=12, blue=14, green=13 rules is {total_gameids}")
    print(f"The total power is {total_pow}")
