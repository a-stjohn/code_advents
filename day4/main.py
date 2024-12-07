def read_grid(input_str):
    """Convert input string to 2D grid of characters."""
    return [list(row.strip()) for row in input_str.strip().split('\n')]


def find_xmas_occurrences(grid):
    """Find all XMAS occurrences in all possible directions."""
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1)
    ]

    reverse_directions = [(dx * -1, dy * -1) for (dx, dy) in directions]
    all_directions = directions + reverse_directions
    print(f"All possible directions: {all_directions}")

    xmas_count = 0

    for r in range(rows):
        for c in range(cols):
            for (dx, dy) in all_directions:
                if 0 <= r + dx * 3 < rows and 0 <= c + dy * 3 < cols:
                    if (grid[r][c] == 'X' and
                            grid[r + dx][c + dy] == 'M' and
                            grid[r + dx * 2][c + dy * 2] == 'A' and
                            grid[r + dx * 3][c + dy * 3] == 'S'):
                        xmas_count += 1

    return xmas_count


def solve_word_search(input_grid):
    """Solve both parts of the word search puzzle."""
    grid = read_grid(input_grid)
    part1_result = find_xmas_occurrences(grid)
    # part2_result = find_x_mas_occurrences(grid)

    # return part1_result, part2_result
    return part1_result


if __name__ == '__main__':
    with open("puzzle_input.txt") as fin:
        word_search_text = fin.read()

    answer = solve_word_search(word_search_text)
    print(answer)
