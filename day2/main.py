def get_puzzle_input():
    with open("puzzle_input.txt") as fin:
        puzzle_input = []
        for line in fin:
            puzzle_input.append(list(map(int, line.split())))

    return puzzle_input


if __name__ == '__main__':
    reports = get_puzzle_input()
    print(reports)
    # print([element1 - element2 for element1, element2 in zip(reports[0], reports[0][1:])])
