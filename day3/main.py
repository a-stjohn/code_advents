import re


def get_puzzle_input() -> list[list]:
    with open("day3/puzzle_input.txt") as fin:
        puzzle_input = []
        for line in fin:
            puzzle_input.append(line)

    return puzzle_input


def get_matches(text_string):
    regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern=regex_pattern, string=text_string)
    matched_text = [match.group() for match in matches]

    return matched_text


if __name__ == "__main__":
    corrupted_instructions = get_puzzle_input()

    cleaned_instructions = [
        get_matches(corrupted_instruction)
        for corrupted_instruction in corrupted_instructions
    ]
    print(len(cleaned_instructions))
