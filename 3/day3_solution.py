"""Solution for Advent of Code 2022 - Day 3"""

from pathlib import Path

current_dir = Path(".")
input_file = current_dir / "day3_input.txt"

with input_file.open() as open_file:
    input_lines = open_file.read().splitlines()

letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters = letters_lower + letters_lower.upper()
letter_priorities = zip(letters, range(1, 53))
priority_map = {lp[0]: lp[1] for lp in letter_priorities}

# Part 1
shared_item_priorities = []
for items in input_lines:
    compartment_1 = items[: int(len(items) / 2)]
    compartment_2 = items[int(len(items) / 2) :]
    shared = set(compartment_1).intersection(set(compartment_2))
    shared_item_priorities.append(priority_map[shared.pop()])

print("Part 1: ", sum(shared_item_priorities))

# Part 2
badge_priorities = []
group = []
for items in input_lines:
    if len(group) < 2:
        group.append(items)
    elif len(group) == 2:
        group.append(items)
        shared = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        badge_priorities.append(priority_map[shared.pop()])
        group = []

print("Part 2: ", sum(badge_priorities))
