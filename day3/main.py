import re

from numpy.ma.core import correlate


def get_puzzle_input() -> list[list]:
    with open("puzzle_input.txt") as fin:
        puzzle_input = ""
        for line in fin:
            puzzle_input += line

    return puzzle_input


def get_matches(text_string):
    regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern=regex_pattern, string=text_string, )
    # this is full match
    # matched_text = [match.group(0) for match in matches]
    # this is group 1 and group 2 match e.g. the numbers only
    matched_text_numbers = [(match.group(1), match.group(2)) for match in matches]

    # return matched_text
    return matched_text_numbers

def multiply_numbers(mul_instructions):
    multiply_results = []
    for pair in mul_instructions:
        multiply_results.append(int(pair[0]) * int(pair[1]))

    return sum(multiply_results)

def get_matches_part_two(text_string):
    pattern = r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))'

    mul_enabled = True
    total_sum = 0

    matches = re.finditer(pattern, text_string)

    for match in matches:
        full_match = match.group()
        print(f"Matching groups are: {match.groups()}")

        # Handle enable/disable instructions
        if full_match == 'do()':
            mul_enabled = True
        elif full_match == "don't()":
            mul_enabled = False

        # Handle mul instruction
        elif full_match.startswith('mul('):
            if mul_enabled:
                # Extract numbers and convert to integers
                num1 = int(match.group(2))
                num2 = int(match.group(3))

                # Multiply and add to total
                result = num1 * num2
                total_sum += result

    return total_sum

if __name__ == "__main__":
    corrupted_instructions = get_puzzle_input()

    cleaned_instructions = get_matches(corrupted_instructions)
    answer = multiply_numbers(cleaned_instructions)
    print(answer)

    answer_part2 = get_matches_part_two(corrupted_instructions)
    print(answer_part2)