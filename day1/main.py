from time import time
from collections import Counter


def get_puzzle_input() -> tuple[list[int], list[int]]:
    with open("puzzle_input.txt") as fin:
        input_array1 = []
        input_array2 = []
        for line in fin:
            left, right = line.split()
            input_array1.append(int(left))
            input_array2.append(int(right))

    input_array1.sort()
    input_array2.sort()

    return input_array1, input_array2


def main_part1(input_array1: list[int], input_array2: list[int]) -> int:
    differences = []
    for left, right in zip(input_array1, input_array2):
        differences.append(abs(left - right))

    answer = sum(differences)

    return answer


def main_part2(input_array1: list[int], input_array2: list[int]) -> int:
    unique_array1 = set(input_array1)
    element_scores = []
    for unique_element in unique_array1:
        matches = 0
        for element in input_array2:
            if unique_element == element:
                matches += 1
        element_scores.append(unique_element * matches)

    answer = sum(element_scores)

    return answer

def main_part2_gpt(input_array1, input_array2):
    right_count = Counter(input_array1)

    # Calculate the similarity score
    score = sum(x * right_count.get(x, 0) for x in input_array2)

    return score


if __name__ == '__main__':
    left_array, right_array = get_puzzle_input()
    start_base1 = time()
    answer1 = main_part1(left_array, right_array)
    print(f"Time to run base1: {time() - start_base1:0.10f}")
    print(f"The answer to part 1 is {answer1}")

    start_base2 = time()
    answer2 = main_part2_gpt(left_array, right_array)
    print(f"Time to run base2: {time() - start_base2:0.10f}")
    print(f"The answer to part 2 is {answer2}")