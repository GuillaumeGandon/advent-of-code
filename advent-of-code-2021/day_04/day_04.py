from itertools import product


def check_number_in_board(board, number):
    for i, j in product(range(len(board)), range(len(board[0]))):
        numb, checked = board[i][j]
        if not checked and numb == number:
            board[i][j][1] = True
            break


def check_if_line_win(line):
    return all(checked for _numb, checked in line)


def check_if_board_win(board):
    return any(check_if_line_win(row) for row in board) or any(
        check_if_line_win(col) for col in map(tuple, zip(*board))
    )


raw_numbers, *raw_boards = open("input").read().split("\n\n")

numbers = tuple(map(int, raw_numbers.split(",")))
boards = tuple(
    [[[int(numb), False] for numb in row.split()] for row in board.strip().split("\n")] for board in raw_boards
)


first_winner = False
for number in numbers:
    for board in boards:
        check_number_in_board(board, number)

        if not first_winner and check_if_board_win(board):
            unmarked_sum = sum(numb for row in board for numb, checked in row if not checked)
            print(f"Answer part one: {number*unmarked_sum}")
            first_winner = True

    if len(boards) == 1 and check_if_board_win(boards[0]):
        unmarked_sum = sum(numb for row in boards[0] for numb, checked in row if not checked)
        print(f"Answer part two: {number*unmarked_sum}")
        break

    boards = tuple(board for board in boards if not check_if_board_win(board))
