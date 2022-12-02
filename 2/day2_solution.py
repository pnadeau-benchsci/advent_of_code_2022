"""Solution for Advent of Code 2022 - Day 2"""

from pathlib import Path

current_dir = Path(".")
input_file = current_dir / "day2_input.txt"

with input_file.open() as open_file:
    input_lines = open_file.read().splitlines()

score_map = {"Rock": 1, "Paper": 2, "Scissors": 3}
outcome_map = {"Loss": 0, "Draw": 3, "Win": 6}


def part_1():
    shape_map = {
        "A": "Rock",
        "X": "Rock",
        "B": "Paper",
        "Y": "Paper",
        "C": "Scissors",
        "Z": "Scissors",
    }

    def get_my_outcome(me, elf):
        if me == elf:
            return "Draw"

        if me == "Rock":
            if elf == "Scissors":
                return "Win"
            else:
                return "Loss"

        if me == "Paper":
            if elf == "Rock":
                return "Win"
            else:
                return "Loss"

        if me == "Scissors":
            if elf == "Paper":
                return "Win"
            else:
                return "Loss"

    my_scores = []
    for line in input_lines:
        elf = shape_map[line[0]]
        me = shape_map[line[2]]
        my_outcome = get_my_outcome(me, elf)
        my_score = score_map[me] + outcome_map[my_outcome]
        my_scores.append(my_score)

    my_total_score = sum(my_scores)
    return my_total_score


def part_2():
    elf_map = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    my_map = {"X": "Loss", "Y": "Draw", "Z": "Win"}

    def get_my_shape(me, elf):
        if me == "Draw":
            return elf

        if elf == "Rock":
            if me == "Loss":
                return "Scissors"
            else:
                return "Paper"

        if elf == "Paper":
            if me == "Loss":
                return "Rock"
            else:
                return "Scissors"

        if elf == "Scissors":
            if me == "Loss":
                return "Paper"
            else:
                return "Rock"

    my_scores = []
    for line in input_lines:
        elf = elf_map[line[0]]
        my_outcome = my_map[line[2]]
        me = get_my_shape(my_outcome, elf)
        my_score = score_map[me] + outcome_map[my_outcome]
        my_scores.append(my_score)

    return sum(my_scores)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
