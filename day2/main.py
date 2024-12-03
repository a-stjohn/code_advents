def get_puzzle_input() -> list[list]:
    with open("puzzle_input.txt") as fin:
        puzzle_input = []
        for line in fin:
            puzzle_input.append(list(map(int, line.split())))

    return puzzle_input


def is_safe(report):
    strictly_increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    strictly_decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))

    return strictly_increasing or strictly_decreasing


def is_safe_with_dampener(report):
    # If the report is already safe, return True
    if is_safe(report):
        return True

    # Try removing each level (one at a time) and check if the remaining report is safe
    for i in range(len(report)):
        # Create a new report with the i-th level removed
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True

    # If no single removal makes it safe, return False
    return False


def main(puzzle_input: list[list]) -> int:
    return sum(1 for report in puzzle_input if is_safe_with_dampener(report))


if __name__ == '__main__':
    reports = get_puzzle_input()
    answer = main(puzzle_input=reports)
    print(f"The answer is {answer}")
