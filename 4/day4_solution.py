"""Solution for Advent of Code 2022 - Day 4"""

from pathlib import Path

current_dir = Path(".")
input_file = current_dir / "day4_input.txt"

with input_file.open() as open_file:
    input_lines = open_file.read().splitlines()


# Part 1
count_fully_contained = 0
for line in input_lines:
    pair = line.split(",")
    elf_1 = pair[0].split("-")
    elf_2 = pair[1].split("-")

    elf_1_set = set(range(int(elf_1[0]), int(elf_1[1]) + 1))
    elf_2_set = set(range(int(elf_2[0]), int(elf_2[1]) + 1))

    if elf_1_set.issubset(elf_2_set) or elf_2_set.issubset(elf_1_set):
        count_fully_contained += 1

print("Part 1: ", count_fully_contained)


# Part 2
count_intersect = 0
for line in input_lines:
    pair = line.split(",")
    elf_1 = pair[0].split("-")
    elf_2 = pair[1].split("-")

    elf_1_set = set(range(int(elf_1[0]), int(elf_1[1]) + 1))
    elf_2_set = set(range(int(elf_2[0]), int(elf_2[1]) + 1))

    if elf_1_set.intersection(elf_2_set):
        count_intersect += 1

print("Part 2: ", count_intersect)
