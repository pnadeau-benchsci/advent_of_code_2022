"""Solution for Advent of Code 2022 - Day 1"""

from pathlib import Path

current_dir = Path(".")
input_file = current_dir / "day1_input.txt"

with input_file.open() as open_file:
    input_lines = open_file.read().splitlines()

elf_total_calories = []
calories = 0
for line in input_lines:
    if line != "":
        calories += int(line)
    else:
        elf_total_calories.append(calories)
        calories = 0

# Part 1
most_calories = max(elf_total_calories)
print(most_calories)

# Part 2
elf_total_calories_sorted = sorted(elf_total_calories)
sum_highest_three = sum(elf_total_calories_sorted[-3:])
print(sum_highest_three)
