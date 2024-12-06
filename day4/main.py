def get_puzzle_input():
    puzzle_matrix = []
    with open("puzzle_input.txt") as fin:
        for line in fin:
            puzzle_matrix.append(line.split("\n")[0])

    return puzzle_matrix


def count_word_in_grid(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Function to check if the word can be found starting from (r, c) in a given direction
    def check_word(r, c, direction):
        dr, dc = direction
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            # Check if the new position is out of bounds or does not match the corresponding character in the word
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Traverse each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell matches the first letter of the word, check in all directions
            if grid[r][c] == word[0]:
                for direction in DIRECTIONS:
                    if check_word(r, c, direction):
                        count += 1

    return count

if __name__ == '__main__':
    DIRECTIONS = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right (diagonal)
        (-1, -1),  # up-left (diagonal)
        (1, -1),  # down-left (diagonal)
        (-1, 1)  # up-right (diagonal)
    ]

    word_search = get_puzzle_input()
    answer = count_word_in_grid(word_search)
    print(answer)