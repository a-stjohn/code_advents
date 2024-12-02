from time import time
import numpy as np


def main() -> int:
    with open("puzzle_input.txt") as fin:
        left_array = []
        right_array = []
        for line in fin:
            left, right = line.split()
            left_array.append(int(left))
            right_array.append(int(right))

    left_array.sort()
    right_array.sort()

    differences = []
    for left, right in zip(left_array, right_array):
        differences.append(abs(left - right))

    answer = sum(differences)

    return answer


def use_numpy() -> int:
    with open("puzzle_input.txt") as fin:
        arrays = []
        for line in fin:
            arrays.append(np.array(object=line.split(), dtype=np.int32))

        input_matrix = np.stack(arrays)
        input_matrix.sort(axis=0)
        print(input_matrix[])


if __name__ == '__main__':
    # start = time()
    # main()
    # print(f"Time to run: {time() - start}")
    # print(f"The answer is {main()}")

    use_numpy()