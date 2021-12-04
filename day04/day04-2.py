def calculate_score(board: list, number: str) -> int:
    score = 0
    for row in board:
        for value, hit in row:
            if not hit:
                score += int(value)
    return score * int(number)


def main() -> None:
    with open('input.txt') as file:
        bingo_data = file.read().splitlines()

    numbers = bingo_data[0].split(',')

    index = 2
    boards = []  # boards will be a list containing 5x5 lists (bingo boards)
    while index < len(bingo_data):
        new_board = []
        for i in range(0, 5):
            row = []
            for field in bingo_data[index + i].split():
                row.append((field, False))
            new_board.append(row)
        boards.append(new_board)
        index += 6

    winning_boards = []
    for number in numbers:
        new_boards = []
        for board in boards:
            mark_board(board, number)
            if check_board(board):
                winning_boards.append((board.copy(), str(number)))
            else:
                new_boards.append(board)
        if not new_boards:
            break
        boards = new_boards

    print(calculate_score(*winning_boards[-1]))


def mark_board(board: list, mark: str) -> None:
    for row in board:
        for i, val in enumerate(row):
            if val[0] == mark:
                row[i] = (val[0], True)


def check_board(board: list) -> bool:
    # check rows
    for row in board:
        if count_hits(row) == 5:
            return True
    # check columns
    for i in range(5):
        column = [x[i] for x in board]
        if count_hits(column) == 5:
            return True
    return False


def count_hits(row: list) -> int:
    hits = 0
    for num, hit in row:
        if hit:
            hits += 1
    return hits


if __name__ == '__main__':
    main()
